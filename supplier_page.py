import streamlit as st
import pandas as pd
import database as db
import re
from datetime import datetime

# --- HELPER: BERSIHKAN HARGA (UNTUK CSV UPLOAD) ---
def clean_currency(value):
    if isinstance(value, str):
        # Hapus "Rp", spasi, titik (jika pemisah ribuan), dll
        # Asumsi format Indonesia: 1.000.000 atau 1000000
        clean_str = re.sub(r'[Rp\s,]', '', value, flags=re.IGNORECASE)
        # Hapus titik hanya jika itu pemisah ribuan (biasanya digit setelah titik ada 3)
        clean_str = clean_str.replace(".", "") 
        return int(clean_str) if clean_str.isdigit() else 0
    return value

# --- HELPER: FORMAT TANGGAL UNTUK NAMA FILE ---
def get_current_time_str():
    return datetime.now().strftime("%Y-%m-%d_%H-%M")

# --- MODAL FORM (POPUP) ---
@st.dialog("Tambah Stok Barang")
def show_add_stock_modal():
    # Pilihan Tab di dalam Modal
    tab_manual, tab_csv = st.tabs(["📝 Input Manual", "📂 Upload CSV"])

    # --- OPSI 1: INPUT MANUAL ---
    # --- OPSI 1: INPUT MANUAL ---
    with tab_manual:
        with st.form("form_tambah_stok"):
            # Load existing items to help autocomplete
            existing_items = db.get_stock_summary()['Nama Barang'].unique().tolist() if not db.get_stock_summary().empty else []
            
            col1, col2 = st.columns(2)
            with col1:
                i_tgl = st.date_input("Tanggal Masuk")
                i_spl = st.text_input("Nama Supplier", placeholder="Contoh: Toko ABC")
                i_kat = st.selectbox("Kategori", ["Bahan Baku Utama", "Bahan Pendukung", "Alat Tulis Kantor", "Jasa", "Lainnya"])
                i_hrg = st.number_input("Harga Satuan (Rp)", min_value=0, step=100)
            with col2:
                # Ganti text_input biasa dengan Selectbox yang bisa diketik (jika Streamlit versi baru)
                # Atau gunakan text_input dengan bantuan di bawahnya
                i_itm = st.text_input("Nama Barang", placeholder="Ketik nama barang...")
                
                i_qty = st.number_input("Quantity", min_value=1, value=1)
                i_sat = st.selectbox("Satuan", ["pcs", "meter", "roll", "kg", "lusin", "gross", "pack", "set", "lembar"])
            
            st.markdown("---")
            if st.form_submit_button("💾 Simpan ke Database", type="primary", use_container_width=True):
                if i_itm and i_spl:
                    if db.insert_data(i_tgl, i_spl, i_kat, i_itm, i_qty, i_sat, i_hrg):
                        st.success(f"Berhasil menambahkan {i_itm}!")
                        st.rerun()

    # --- OPSI 2: UPLOAD CSV ---
    with tab_csv:
        st.info("Pastikan format CSV memiliki header: Tanggal, Supplier, Kategori, Item, Qty, Satuan, Harga")
        uploaded_file = st.file_uploader("Pilih file CSV", type=["csv"])
        
        if uploaded_file is not None:
            try:
                df_upload = pd.read_csv(uploaded_file)
                st.write(f"Terbaca {len(df_upload)} baris data.")
                
                # Preview Data
                st.dataframe(df_upload.head(3), use_container_width=True)

                if st.button("🚀 Proses Import CSV", type="primary", use_container_width=True):
                    success_count = 0
                    fail_count = 0
                    progress_bar = st.progress(0)

                    for index, row in df_upload.iterrows():
                        try:
                            # Mapping kolom CSV (Sesuaikan jika nama header beda)
                            # Menggunakan .get() agar tidak error jika kolom beda dikit
                            # Asumsi header CSV user: TANGGAL PEMBELIAN, NAMA SUPPLIER, dll.
                            
                            # Coba parsing tanggal
                            raw_tgl = str(row.get('TANGGAL PEMBELIAN', row.get('Tanggal', '')))
                            try:
                                t_tgl = pd.to_datetime(raw_tgl, dayfirst=True).date()
                            except:
                                t_tgl = pd.to_datetime("today").date()

                            t_spl = row.get('NAMA SUPPLIER & PENYEDIA JASA', row.get('Supplier', '-'))
                            t_kat = row.get('KATEGORI ITEM', row.get('Kategori', 'Umum'))
                            t_itm = row.get('ITEM', row.get('Item', 'Unknown'))
                            t_qty = int(row.get('QTY', row.get('Qty', 0)))
                            t_sat = row.get('SATUAN', row.get('Satuan', 'pcs'))
                            
                            # Bersihkan harga
                            raw_hrg = str(row.get('HARGA', row.get('Harga', '0')))
                            t_hrg = clean_currency(raw_hrg)

                            # Insert ke DB
                            if db.insert_data(t_tgl, t_spl, t_kat, t_itm, t_qty, t_sat, t_hrg):
                                success_count += 1
                            else:
                                fail_count += 1
                        except Exception as e:
                            fail_count += 1
                        
                        # Update progress bar
                        progress_bar.progress((index + 1) / len(df_upload))

                    st.success(f"Selesai! Berhasil: {success_count}, Gagal: {fail_count}")
                    if success_count > 0:
                        st.rerun()

            except Exception as e:
                st.error(f"Gagal memproses CSV: {e}")

# --- HALAMAN UTAMA ---
def show():
    st.title("Gudang & Inventaris")
    
    # --- TABS NAVIGATION ---
    tab_main, tab_in, tab_out = st.tabs(["📦 Stok Gudang", "📥 Riwayat Masuk", "📤 Riwayat Keluar"])

    # === TAB 1: MAIN TABLE (STOK SAAT INI) ===
    with tab_main:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        
        # HEADER DENGAN TOMBOL ADD
        col_header, col_btn = st.columns([3, 1])
        with col_header:
            st.subheader("Daftar Ketersediaan Barang")
            st.caption("Tabel ini menampilkan stok yang tersedia di gudang saat ini.")
        with col_btn:
            # TOMBOL UNTUK MEMBUKA MODAL
            if st.button("➕ Tambah Stok", type="primary", use_container_width=True):
                show_add_stock_modal()

        # 1. Load Data Summary
        df_summary = db.get_stock_summary()
        
        if not df_summary.empty:
            # 2. FILTER LAYOUT
            col_search, col_filter = st.columns([3, 1])
            with col_search:
                search = st.text_input("🔍 Cari Barang:", placeholder="Ketik nama item...", key="search_main")
            with col_filter:
                list_kategori = ["Semua"] + df_summary['Kategori'].unique().tolist()
                filter_kat = st.selectbox("Filter Kategori:", list_kategori, key="filter_kategori_main")

            # 3. TERAPKAN FILTER
            if filter_kat != "Semua":
                df_summary = df_summary[df_summary['Kategori'] == filter_kat]
            if search:
                df_summary = df_summary[df_summary['Nama Barang'].str.contains(search, case=False)]
            
            # 4. TAMPILKAN TABEL
            st.dataframe(
                df_summary,
                use_container_width=True,
                hide_index=True,
                height=500,
                column_config={
                    "Stok Tersedia": st.column_config.NumberColumn("Stok Tersedia", format="%d")
                }
            )

            # --- EXPORT BUTTON (TAB 1) ---
            st.markdown("### 🖨️ Export Laporan Stok")
            csv_data = df_summary.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Laporan Stok (CSV)",
                data=csv_data,
                file_name=f"laporan_stok_gudang_{get_current_time_str()}.csv",
                mime="text/csv",
                help="Klik untuk mengunduh laporan stok saat ini dalam format CSV (bisa dibuka di Excel)"
            )

        else:
            st.info("Belum ada data stok (atau semua stok habis).")
        st.markdown('</div>', unsafe_allow_html=True)

    # === TAB 2: RIWAYAT MASUK (STOCK IN HISTORY) ===
    # === TAB 2: RIWAYAT MASUK (STOCK IN HISTORY) ===
    with tab_in:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        c1, c2 = st.columns([4, 1])
        with c1:
            st.subheader("📥 Histori Barang Masuk")
            st.caption("Ini adalah daftar transaksi. Jika ada salah input, hapus datanya di sini.")
        with c2:
            if st.button("🔄 Refresh", key="btn_refresh_in"):
                st.rerun()

        # 1. AMBIL DATA
        df_in = db.get_stock_ins_history()
        
        if not df_in.empty:
            # 2. TAMPILKAN TABEL
            # Kita butuh kolom ID untuk fitur delete, tapi disembunyikan di tampilan agar rapi
            st.dataframe(
                df_in,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "id": None, # Sembunyikan ID
                    "tanggal": st.column_config.DateColumn("Tanggal Beli"),
                    "qty": st.column_config.NumberColumn("Quantity"),
                    "harga": st.column_config.NumberColumn("Harga", format="Rp %d")
                }
            )

            # --- EXPORT BUTTON (TAB 2) ---
            st.markdown("### 🖨️ Export Laporan Masuk")
            csv_in = df_in.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Riwayat Masuk (CSV)",
                data=csv_in,
                file_name=f"laporan_barang_masuk_{get_current_time_str()}.csv",
                mime="text/csv"
            )

            # 3. FITUR DELETE (EXPANDER)
            st.markdown("---")
            with st.expander("🗑️ Hapus Data Salah (Klik disini)"):
                st.warning("Hati-hati! Data yang dihapus akan mengurangi stok di halaman utama.")
                
                # Buat list pilihan yang mudah dibaca user: "ID - Item - Qty"
                # Format: "12 | Kain Drill (10 pcs)"
                df_in['label'] = df_in.apply(lambda x: f"{x['id']} | {x['item']} ({x['qty']} {x['satuan']}) - {x['tanggal']}", axis=1)
                
                pilih_hapus = st.selectbox("Pilih Transaksi untuk Dihapus:", df_in['label'])
                
                if st.button("❌ Hapus Transaksi Ini", type="primary"):
                    # Ambil ID dari string label (angka sebelum tanda |)
                    id_to_delete = int(pilih_hapus.split(" | ")[0])
                    
                    if db.delete_inventory_log(id_to_delete):
                        st.success("Data berhasil dihapus!")
                        st.rerun() # Auto Refresh Halaman
                    else:
                        st.error("Gagal menghapus data.")

        else:
            st.warning("Belum ada data pemasukan.")
        st.markdown('</div>', unsafe_allow_html=True)

    # === TAB 3: RIWAYAT KELUAR (STOCK OUT HISTORY) ===
    with tab_out:
        col_form, col_data = st.columns([1, 2])
        
        # Form Input Barang Keluar
        with col_form:
            st.markdown('<div class="white-card">', unsafe_allow_html=True)
            st.markdown("#### Catat Penggunaan")
            with st.form("form_out"):
                list_items = df_summary['Nama Barang'].unique().tolist() if not df_summary.empty else []
                # Ambil list unit unik dari DB agar user bisa milih satuan yang sesuai
                list_units = df_summary['Satuan'].unique().tolist() if not df_summary.empty else []
                
                o_tgl = st.date_input("Tanggal Keluar")
                o_itm = st.selectbox("Nama Barang", list_items)
                o_qty = st.number_input("Jumlah Terpakai", min_value=1, value=1)
                o_unit = st.selectbox("Satuan", list_units) 
                o_ket = st.text_input("Nama Project / Keterangan", placeholder="Contoh: Seragam SD...")
                
                if st.form_submit_button("Simpan Data Keluar", type="primary", use_container_width=True):
                    if db.insert_stock_out(o_tgl, o_itm, o_qty, o_unit, o_ket):
                        st.success("Berhasil disimpan!")
                        st.rerun()
            st.markdown('</div>', unsafe_allow_html=True)
            
        # Tabel Data Keluar
        with col_data:
            st.markdown('<div class="white-card">', unsafe_allow_html=True)
            st.subheader("📤 Log Barang Keluar")
            df_out = db.get_stock_outs_history()
            
            if not df_out.empty:
                st.dataframe(
                    df_out,
                    use_container_width=True,
                    hide_index=True,
                    column_config={
                        "tanggal": st.column_config.DateColumn("Tanggal"),
                        "qty": st.column_config.NumberColumn("Qty Keluar")
                    }
                )

                # --- EXPORT BUTTON (TAB 3) ---
                st.markdown("### 🖨️ Export Laporan Keluar")
                csv_out = df_out.to_csv(index=False).encode('utf-8')
                st.download_button(
                    label="📥 Download Riwayat Keluar (CSV)",
                    data=csv_out,
                    file_name=f"laporan_barang_keluar_{get_current_time_str()}.csv",
                    mime="text/csv"
                )
                
            else:
                st.info("Belum ada barang keluar tercatat.")
            st.markdown('</div>', unsafe_allow_html=True)