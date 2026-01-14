import mysql.connector
import pandas as pd
import streamlit as st

def get_db_connection():
    try:
        return mysql.connector.connect(
            host="localhost", user="root", password="", database="db_inventory"
        )
    except mysql.connector.Error as e:
        st.error(f"Error connecting to database: {e}")
        return None

# --- FUNGSI UNTUK HALAMAN UTAMA (STOK SAAT INI) ---
def get_stock_summary():
    conn = get_db_connection()
    if conn:
        # 1. Ambil Total Masuk per Item
        query_in = """
            SELECT item, kategori, satuan, SUM(qty) as total_masuk 
            FROM inventory_logs 
            GROUP BY item, kategori, satuan
        """
        df_in = pd.read_sql(query_in, conn)
        
        # 2. Ambil Total Keluar per Item
        query_out = "SELECT item, SUM(qty) as total_keluar FROM stock_outs GROUP BY item"
        df_out = pd.read_sql(query_out, conn)
        
        conn.close()
        
        # 3. Gabungkan (Merge)
        if not df_in.empty:
            if not df_out.empty:
                # Join data masuk dan keluar berdasarkan Nama Item
                df_merged = pd.merge(df_in, df_out, on='item', how='left')
                df_merged['total_keluar'] = df_merged['total_keluar'].fillna(0)
            else:
                df_merged = df_in
                df_merged['total_keluar'] = 0
            
            # Hitung Stok Akhir
            df_merged['stok_saat_ini'] = df_merged['total_masuk'] - df_merged['total_keluar']
            
            # Bersihkan kolom untuk tabel utama
            final_df = df_merged[['item', 'kategori', 'satuan', 'stok_saat_ini']]
            final_df.columns = ['Nama Barang', 'Kategori', 'Satuan', 'Stok Tersedia']
            return final_df
            
    return pd.DataFrame()

# --- FUNGSI RIWAYAT (LOGS) ---
def get_stock_ins_history():
    conn = get_db_connection()
    if conn:
        df = pd.read_sql("SELECT id, tanggal, supplier, item, qty, harga FROM inventory_logs ORDER BY tanggal DESC", conn)
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

# --- FUNGSI INPUT ---
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

def insert_data(tgl, spl, kat, itm, qty, sat, hrg):
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        sql = """
            INSERT INTO inventory_logs (tanggal, supplier, kategori, item, qty, satuan, harga) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        val = (tgl, spl, kat, itm, qty, sat, hrg)
        cur.execute(sql, val)
        conn.commit()
        conn.close()
        return True
    return False

def update_data(id_b, tgl, spl, kat, itm, qty, sat, hrg):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        sql = """
            UPDATE inventory_logs 
            SET tanggal=%s, supplier=%s, kategori=%s, item=%s, qty=%s, satuan=%s, harga=%s 
            WHERE id=%s
        """
        val = (tgl, spl, kat, itm, qty, sat, hrg, id_b)
        cursor.execute(sql, val)
        conn.commit()
        conn.close()
        return True
    return False

def delete_data(id_b):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM inventory_logs WHERE id=%s", (id_b,))
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
