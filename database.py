import mysql.connector
import pandas as pd
import streamlit as st
import os

def get_db_connection():
    try:
        return mysql.connector.connect(
            host="localhost", user="root", password="", database="db_inventory"
        )
    except mysql.connector.Error as e:
        st.error(f"Error connecting to database: {e}")
        return None
# --- FUNGSI KHUSUS DASHBOARD ---

# --- FUNGSI KHUSUS DASHBOARD (UPDATED) ---
def get_dashboard_metrics():
    conn = get_db_connection()
    metrics = {
        "total_asset": 0,
        "total_tailors": 0,
        "items_sold": 0,          # Ini sekarang akan berisi Data Penjualan 2025
        "top_supplier": "-",      
        "top_supplier_vol": 0,    
        "low_stock_count": 0
    }
    
    if conn:
        # 1. Hitung Total Aset
        df_stock = get_stock_summary() 
        df_prices = pd.read_sql("SELECT item, AVG(harga) as avg_price FROM inventory_logs GROUP BY item", conn)
        
        if not df_stock.empty and not df_prices.empty:
            df_stock = df_stock.merge(df_prices, left_on='Nama Barang', right_on='item', how='left')
            df_stock['valuation'] = df_stock['Stok Tersedia'] * df_stock['avg_price']
            metrics['total_asset'] = df_stock['valuation'].sum()
            metrics['low_stock_count'] = len(df_stock[df_stock['Stok Tersedia'] < 10])

        # 2. Hitung Total Penjahit
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM tailors")
        result_tailor = cur.fetchone()
        if result_tailor:
            metrics['total_tailors'] = result_tailor[0]

        # 3. Hitung TOTAL PENJUALAN TAHUN 2025 (LOGIC BARU)
        # Kita ambil dari file eksternal karena 'stock_outs' adalah pemakaian bahan, bukan penjualan produk.
        try:
            # OPSI A: Coba baca dari file Rekap Bulanan (yang dipakai di chart)
            if os.path.exists("Total quantity monthly.xlsx"):
                df_sales = pd.read_excel("Total quantity monthly.xlsx")
                # Filter hanya tahun 2025 dan sum QTY
                # Pastikan nama kolom di Excel sesuai (misal: 'YEAR' dan 'QTY')
                total_2025 = df_sales[df_sales['YEAR'] == 2025]['SUM of QTY'].sum()
                metrics['items_sold'] = total_2025
            
            # OPSI B: Jika Excel tidak ada, coba baca CSV Raw 2025
            elif os.path.exists("Dataset - Supplier and stocks - project recap 2025 (cleaned).csv"):
                df_raw = pd.read_csv("Dataset - Supplier and stocks - project recap 2025 (cleaned).csv")
                metrics['items_sold'] = df_raw['QTY'].sum()
                
            else:
                metrics['items_sold'] = 0
                
        except Exception as e:
            print(f"Error calculating sales 2025: {e}")
            metrics['items_sold'] = 0

        # 4. Hitung TOP SUPPLIER (NEW)
        # Mengurutkan supplier berdasarkan total qty barang yang mereka kirim
        query_supp = """
            SELECT supplier, SUM(qty) as total_supply 
            FROM inventory_logs 
            GROUP BY supplier 
            ORDER BY total_supply DESC 
            LIMIT 1
        """
        df_supp = pd.read_sql(query_supp, conn)
        
        if not df_supp.empty:
            metrics['top_supplier'] = df_supp.iloc[0]['supplier']
            metrics['top_supplier_vol'] = df_supp.iloc[0]['total_supply']
        
        conn.close()
    
    return metrics

def get_monthly_sales_data():
    conn = get_db_connection()
    if conn:
        # Mengambil data summary bulanan (Jika table sales_summary_monthly sudah diisi)
        # Jika belum ada, kita bisa hitung on-the-fly dari stock_outs
        query = """
            SELECT DATE_FORMAT(tanggal, '%Y-%m') as month_year, SUM(qty) as total_qty 
            FROM stock_outs 
            GROUP BY month_year 
            ORDER BY month_year
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    return pd.DataFrame()

# --- FUNGSI HALAMAN UTAMA (STOK) - SMART AGGREGATION ---
def get_stock_summary():
    conn = get_db_connection()
    if conn:
        # 1. AMBIL SEMUA DATA MENTAH (JANGAN GROUP BY DI SQL)
        # Kita ambil raw data agar bisa dibersihkan di Python
        query_in = "SELECT item, kategori, satuan, qty FROM inventory_logs"
        df_in = pd.read_sql(query_in, conn)
        
        query_out = "SELECT item, qty, satuan FROM stock_outs"
        df_out = pd.read_sql(query_out, conn)
        
        conn.close()
        
        # 2. PROSES DATA MASUK (IN)
        if not df_in.empty:
            # BERSIHKAN TEXT (Normalization)
            # Ini akan menyatukan "Kain Drill", "kain drill", "KAIN DRILL " menjadi satu
            df_in['item'] = df_in['item'].str.strip().str.title()
            df_in['satuan'] = df_in['satuan'].str.strip().str.lower()
            df_in['kategori'] = df_in['kategori'].str.strip().str.title()
            
            # GROUP BY di PANDAS
            df_in_grouped = df_in.groupby(['item', 'kategori', 'satuan'])['qty'].sum().reset_index()
            df_in_grouped.rename(columns={'qty': 'total_masuk'}, inplace=True)
        else:
            df_in_grouped = pd.DataFrame(columns=['item', 'kategori', 'satuan', 'total_masuk'])

        # 3. PROSES DATA KELUAR (OUT)
        if not df_out.empty:
            # Bersihkan text agar match dengan data masuk
            df_out['item'] = df_out['item'].str.strip().str.title()
            df_out['satuan'] = df_out['satuan'].str.strip().str.lower()
            
            # Group by Item (Simple version)
            # Jika user salah input satuan saat keluar, kita tetap kurangi stok berdasarkan Nama Barang
            df_out_grouped = df_out.groupby('item')['qty'].sum().reset_index()
            df_out_grouped.rename(columns={'qty': 'total_keluar'}, inplace=True)
        else:
            df_out_grouped = pd.DataFrame(columns=['item', 'total_keluar'])
        
        # 4. GABUNGKAN (MERGE)
        if not df_in_grouped.empty:
            # Join berdasarkan Nama Barang
            df_merged = pd.merge(df_in_grouped, df_out_grouped, on='item', how='left')
            df_merged['total_keluar'] = df_merged['total_keluar'].fillna(0)
            
            # Hitung Stok Akhir
            df_merged['stok_saat_ini'] = df_merged['total_masuk'] - df_merged['total_keluar']
            
            # Filter Stok > 0
            df_merged = df_merged[df_merged['stok_saat_ini'] > 0]
            
            # Formatting Akhir
            final_df = df_merged[['item', 'kategori', 'stok_saat_ini', 'satuan']]
            final_df.columns = ['Nama Barang', 'Kategori', 'Stok Tersedia', 'Satuan']
            
            return final_df
            
    return pd.DataFrame()

# --- FUNGSI RIWAYAT ---
def get_stock_ins_history():
    conn = get_db_connection()
    if conn:
        # Update: Tambahkan 'satuan' ke query
        df = pd.read_sql("SELECT id, tanggal, supplier, item, qty, satuan, harga FROM inventory_logs ORDER BY tanggal DESC", conn)
        conn.close()
        return df
    return pd.DataFrame()

def get_stock_outs_history():
    conn = get_db_connection()
    if conn:
        df = pd.read_sql("SELECT id, tanggal, item, qty, satuan, keterangan as project FROM stock_outs ORDER BY tanggal DESC", conn)
        conn.close()
        return df
    return pd.DataFrame()

# --- FUNGSI INPUT (Tidak Berubah) ---
def insert_stock_out(tgl, itm, qty, unit, proj):
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        sql = "INSERT INTO stock_outs (tanggal, item, qty, satuan, keterangan) VALUES (%s, %s, %s, %s, %s)"
        cur.execute(sql, (tgl, itm, qty, unit, proj))
        conn.commit()
        conn.close()
        return True
    return False

# --- FUNGSI INPUT (Updated with Text Cleaning) ---
def insert_data(tgl, spl, kat, itm, qty, sat, hrg):
    conn = get_db_connection()
    if conn:
        # 1. BERSIHKAN TEKS (Normalization)
        # Agar "Kain drill", "KAIN DRILL", "Kain Drill " dianggap sama
        clean_item = itm.strip().title()       # Contoh: " kain drill " -> "Kain Drill"
        clean_kat = kat.strip().title()        # Contoh: "BAHAN BAKU" -> "Bahan Baku"
        clean_spl = spl.strip()                # Hapus spasi depan/belakang
        clean_sat = sat.strip().lower()        # Satuan jadi huruf kecil semua (pcs, kg)

        cur = conn.cursor()
        sql = """
            INSERT INTO inventory_logs (tanggal, supplier, kategori, item, qty, satuan, harga) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        # Gunakan variable yang sudah dibersihkan (clean_...)
        cur.execute(sql, (tgl, clean_spl, clean_kat, clean_item, qty, clean_sat, hrg))
        conn.commit()
        conn.close()
        return True
    return False

def load_data():
    conn = get_db_connection()
    if conn:
        # Load data, urutkan dari yang terbaru
        df = pd.read_sql("SELECT * FROM inventory_logs ORDER BY tanggal DESC", conn)
        conn.close()
        return df
    return pd.DataFrame()


# --- FUNGSI UNTUK HALAMAN PENJAHIT / KARYAWAN ---
def insert_penjahit(
    kode_penjahit, nama, nik, alamat, kecamatan, usia,
    kerapian, ketepatan_waktu, quantity, komitmen,
    spesialis, status_km
):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
        INSERT INTO tailors (
            kode_penjahit, nama, nik, alamat, kecamatan, usia,
            kerapian, ketepatan_waktu, quantity, komitmen,
            spesialis, status_keluarga_miskin
        )
        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(sql, (
            kode_penjahit, nama, nik, alamat, kecamatan, usia,
            kerapian, ketepatan_waktu, quantity, komitmen,
            spesialis, status_km
        ))
        conn.commit()
        return True
    except Exception as e:
        print("DB Error:", e)
        return False

def get_all_karyawan():
    conn = get_db_connection()
    query = """
    SELECT
        kode_penjahit AS "Kode Penjahit",
        nama AS "Nama",
        nik AS "NIK",
        alamat AS "Alamat",
        kecamatan AS "Kecamatan",
        usia AS "Usia",
        kerapian AS "Kerapian",
        ketepatan_waktu AS "Ketepatan Waktu",
        quantity AS "Quantity",
        komitmen AS "Komitmen",
        COALESCE(spesialis, 'N/A') AS "Spesialis",
        COALESCE(status_keluarga_miskin, 'N/A') AS "Status Keluarga Miskin"
    FROM tailors
    ORDER BY nama
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# --- FUNGSI UNTUK HALAMAN PENJUALAN / SALES ---
def insert_sales_monthly(year, month, month_name, item_count, total_qty):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO sales_summary_monthly
        (year, month, month_name, item_count, total_qty)
        VALUES (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            year,
            month,
            month_name,
            item_count,
            total_qty
        ))

        conn.commit()
        cursor.close()
        conn.close()
        return True

    except Exception as e:
        print("DB Error:", e)
        return False

def get_sales_monthly():
    conn = get_db_connection()
    query = """
        SELECT
            year AS "Tahun",
            month AS "Bulan (Angka)",
            month_name AS "Bulan",
            item_count AS "Jumlah Item",
            total_qty AS "Total Qty"
        FROM sales_summary_monthly
        ORDER BY year, month
    """
    df = pd.read_sql(query, conn)
    conn.close()
    return df




# --- TAMBAHKAN FUNGSI INI DI PALING BAWAH database.py ---

def delete_inventory_log(id_log):
    conn = get_db_connection()
    if conn:
        try:
            cur = conn.cursor()
            # Hapus baris berdasarkan ID
            cur.execute("DELETE FROM inventory_logs WHERE id = %s", (id_log,))
            conn.commit()
            conn.close()
            return True
        except mysql.connector.Error as e:
            st.error(f"Gagal menghapus: {e}")
            return False
    return False