import streamlit as st
import mysql.connector
import pandas as pd
from datetime import date
# IMPORT LIBRARY BARU INI
from streamlit_option_menu import option_menu

# --- 1. CONFIG HALAMAN ---
st.set_page_config(
    page_title="Inventory System",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CSS CUSTOM (Penyempurnaan Tampilan) ---
st.markdown("""
    <style>
    .stApp { background-color: #f8f9fa; }
    
    /* Menghilangkan padding atas agar navbar terlihat lebih menyatu */
    .block-container { padding-top: 2rem; }
    
    /* Styling Kartu Statistik */
    [data-testid="stMetric"] {
        background-color: white;
        border-radius: 10px;
        border-left: 5px solid #3498db;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        padding: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# --- 3. KONEKSI DATABASE ---
def get_db_connection():
    try:
        return mysql.connector.connect(
            host="localhost", user="root", password="", database="db_inventory"
        )
    except mysql.connector.Error:
        return None

# --- 4. MODAL INPUT ---
@st.dialog("Input Stok")
def input_modal():
    with st.form("form_tambah"):
        tgl = st.date_input("Tanggal", date.today())
        spl = st.text_input("Supplier")
        itm = st.text_input("Item")
        qty = st.number_input("Qty", 1)
        hrg = st.number_input("Harga", 0, step=1000)
        ket = st.text_input("Ket")
        if st.form_submit_button("Simpan", type="primary"):
            conn = get_db_connection()
            if conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO stok_barang (tanggal_pembelian, supplier, item, quantity, harga, keterangan) VALUES (%s,%s,%s,%s,%s,%s)", (tgl, spl, itm, qty, hrg, ket))
                conn.commit()
                conn.close()
                st.success("Berhasil!")
                st.rerun()

# --- 5. HALAMAN DASHBOARD ---
def show_dashboard():
    col1, col2 = st.columns([3, 1])
    with col1:
        st.title("📊 Dashboard")
    with col2:
        if st.button("➕ Tambah Data", type="primary", use_container_width=True):
            input_modal()

    conn = get_db_connection()
    if conn:
        df = pd.read_sql("SELECT * FROM stok_barang ORDER BY tanggal_pembelian DESC", conn)
        conn.close()
        
        if not df.empty:
            # Cards
            c1, c2, c3 = st.columns(3)
            c1.metric("Total Aset", f"Rp {(df['quantity'] * df['harga']).sum():,.0f}")
            c2.metric("Total Item", f"{df['quantity'].sum()} Unit")
            c3.metric("Supplier", f"{df['supplier'].nunique()} Mitra")
            
            # Table
            st.markdown("### Transaksi Terakhir")
            df['Total'] = df['quantity'] * df['harga']
            st.dataframe(df, use_container_width=True, hide_index=True)
        else:
            st.info("Data kosong.")

# --- 6. HALAMAN SUPPLIER ---
def show_supplier():
    st.title("🚚 Data Supplier")
    conn = get_db_connection()
    if conn:
        df = pd.read_sql("SELECT supplier, COUNT(*) as transaksi FROM stok_barang GROUP BY supplier", conn)
        conn.close()
        st.dataframe(df, use_container_width=True, hide_index=True)

# --- 7. MAIN (NAVIGASI BARU) ---
def main():
    # SIDEBAR DENGAN OPTION MENU
    with st.sidebar:
        # Ini adalah pengganti st.radio yang jauh lebih bagus
        selected = option_menu(
            menu_title="INVENTKU",  # Judul Menu
            options=["Dashboard", "Supplier", "Laporan"],  # Pilihan
            icons=["house", "truck", "file-earmark-text"], # Ikon Bootstrap (https://icons.getbootstrap.com/)
            menu_icon="box-seam",   # Ikon Judul
            default_index=0,        # Halaman awal
            styles={
                "container": {"padding": "5!important", "background-color": "transparent"},
                "icon": {"color": "orange", "font-size": "18px"}, 
                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#34495e", "color": "white"},
                "nav-link-selected": {"background-color": "#3498db"}, # Warna saat dipilih
            }
        )
        
        st.markdown("---")
        st.caption("© 2026 Inventory System")

    # LOGIKA PINDAH HALAMAN
    if selected == "Dashboard":
        show_dashboard()
    elif selected == "Supplier":
        show_supplier()
    elif selected == "Laporan":
        st.title("📄 Laporan")
        st.write("Halaman laporan...")

if __name__ == "__main__":
    main()