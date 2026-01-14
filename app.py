import streamlit as st
from streamlit_option_menu import option_menu
import styles
import dashboard_page
import supplier_page
import tailor_page
import sales_page

# 1. Konfigurasi Halaman (Wajib di baris pertama)
st.set_page_config(
    page_title="Sistem Koperasi",
    page_icon="🏢",
    layout="wide"
)

# 2. Load CSS Styles
styles.load_css()

def main():
    # --- SIDEBAR MENU ---
    with st.sidebar:
        col_kiri, col_tengah, col_kanan = st.columns([1, 2, 1])
        
        with col_tengah:
            # Ganti "logo.png" dengan nama file gambar Anda
            # Jika belum ada gambar, bisa pakai URL contoh di bawah ini:
            st.image("logo koperasi.png", use_container_width=True)
        
        # 3. MENU NAVIGASI (Biarkan seperti sebelumnya)
        selected = option_menu(
            menu_title=None,
            options=["Dashboard", "Gudang", "Karyawan", "Penjualan"],
            icons=["grid", "box-seam", "people", "cart"], 
            default_index=0,
            styles={
                "container": {"padding": "0!important", "background-color": "#d1fae5"},
                "icon": {"color": "#047857", "font-size": "16px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin": "0px", "color": "#064e3b"},
                "nav-link-selected": {"background-color": "#059669", "color": "white"},
            }
        )
        st.markdown("<h2 style='text-align: center; color: #064e3b;'>KOPERASI SUMBER MULIA BAROKAH</h2>", unsafe_allow_html=True)

    # --- ROUTING HALAMAN ---
    
    if selected == "Dashboard":
        dashboard_page.show()

    elif selected == "Gudang":
        supplier_page.show()

    elif selected == "Karyawan":
        tailor_page.show()

    elif selected == "Penjualan":
        sales_page.show()

if __name__ == "__main__":
    main()