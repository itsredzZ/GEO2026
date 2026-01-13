import streamlit as st
import pandas as pd
import database as db

def show():
    st.title("Gudang & Inventaris")
    
    # --- TABS NAVIGATION ---
    tab_main, tab_in, tab_out = st.tabs(["📦 Stok Gudang", "📥 Riwayat Masuk", "📤 Riwayat Keluar"])

    # === TAB 1: MAIN TABLE (STOK SAAT INI) ===
    with tab_main:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        st.subheader("Daftar Ketersediaan Barang")
        st.caption("Tabel ini menampilkan total stok akumulasi per item (Tanpa detail tanggal).")
        
        # Load Data Summary (Group by Item)
        df_summary = db.get_stock_summary()
        
        if not df_summary.empty:
            # Search Filter
            search = st.text_input("🔍 Cari Barang:", placeholder="Ketik nama item...", key="search_main")
            if search:
                df_summary = df_summary[df_summary['Nama Barang'].str.contains(search, case=False)]
            
            # Tampilkan Tabel (White & Readable)
            st.dataframe(
                df_summary,
                use_container_width=True,
                hide_index=True,
                height=500,
                column_config={
                    "Stok Tersedia": st.column_config.NumberColumn(
                        "Stok Tersedia",
                        help="Total Masuk - Total Keluar",
                        format="%d"
                    )
                }
            )
        else:
            st.info("Belum ada data stok.")
        st.markdown('</div>', unsafe_allow_html=True)

    # === TAB 2: RIWAYAT MASUK (STOCK IN HISTORY) ===
    with tab_in:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        c1, c2 = st.columns([4, 1])
        with c1:
            st.subheader("📥 Histori Barang Masuk")
        with c2:
            if st.button("➕ Input Baru", key="btn_add_in"):
                st.toast("Gunakan form di tab 'Input' (jika ada) atau buat modal dialog.")

        df_in = db.get_stock_ins_history()
        
        if not df_in.empty:
            st.dataframe(
                df_in,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "tanggal": st.column_config.DateColumn("Tanggal Beli"),
                    "harga": st.column_config.NumberColumn("Harga", format="Rp %d")
                }
            )
        else:
            st.warning("Belum ada data pemasukan.")
        st.markdown('</div>', unsafe_allow_html=True)

    # === TAB 3: RIWAYAT KELUAR (STOCK OUT HISTORY) ===
    with tab_out:
        col_form, col_data = st.columns([1, 2])
        
        # Form Input Barang Keluar (Manual untuk saat ini)
        with col_form:
            st.markdown('<div class="white-card">', unsafe_allow_html=True)
            st.markdown("#### Catat Penggunaan")
            with st.form("form_out"):
                # Ambil list item dari database agar user tidak typo
                list_items = df_summary['Nama Barang'].unique().tolist() if not df_summary.empty else []
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
            else:
                st.info("Belum ada barang keluar tercatat.")
            st.markdown('</div>', unsafe_allow_html=True)