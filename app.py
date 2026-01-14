import streamlit as st
from streamlit_option_menu import option_menu
import styles
import dashboard_page
import supplier_page
import tailor_page
import sales_page

# 1. Konfigurasi Halaman (Wajib di baris pertama)
st.set_page_config(
    page_title="StockID - Sistem Koperasi",
    page_icon="🏢",
    layout="wide"
)

# 2. Load CSS Styles
styles.load_css()

def main():
    # --- SIDEBAR MENU ---
    with st.sidebar:
        # Ratio 1:6:1 means the image takes up ~75% of the sidebar width
        col_kiri, col_tengah, col_kanan = st.columns([1, 6, 1])
        
        with col_tengah:
            # Pastikan file gambar ini ada di folder yang sama
            try:
                st.image("logo koperasi.png", use_container_width=True)
            except:
                st.header("StockID") # Fallback jika gambar error
        
        # 3. MENU NAVIGASI
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
        
        # Optional: Sidebar Footer (Versi Kecil)
        st.markdown("""
            <div style="position: fixed; bottom: 20px; width: 100%; text-align: left; color: #064e3b; font-size: 12px; padding-left: 20px;">
                StockID v1.0
            </div>
        """, unsafe_allow_html=True)

    # --- ROUTING HALAMAN ---
    
    if selected == "Dashboard":
        dashboard_page.show()

    elif selected == "Gudang":
        supplier_page.show()

    elif selected == "Karyawan":
        tailor_page.show()

    elif selected == "Penjualan":
        sales_page.show()

    # --- FOOTER SECTION (Global Footer) ---
    st.markdown("""
    <div style='text-align: center; margin-top: 50px; padding-top: 20px; border-top: 1px solid #e2e8f0; color: #64748b;'>
        <p style='margin-bottom: 5px; font-weight: 600;'>StockID &copy; 2026</p>
        <p style='font-size: 12px;'>Sistem Manajemen Inventaris & Koperasi Sumber Mulia Barokah</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()