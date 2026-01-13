import streamlit as st
from streamlit_option_menu import option_menu
import styles
import dashboard_page
import supplier_page  # Halaman ini sekarang akan menjadi 'Gudang'

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
        # Kita panggil halaman supplier lama, tapi nanti judulnya kita ganti
        supplier_page.show()

    elif selected == "Karyawan":
        # Placeholder untuk halaman Karyawan (Tabel Penjahit)
        st.markdown("""
            <div class="white-card">
                <div style="background-color: #f1f5f9; padding: 15px 20px; border-bottom: 1px solid #e2e8f0;">
                    <h2 style="margin: 0; font-size: 20px; color: #064e3b;">👥 Data Karyawan & Penjahit</h2>
                </div>
                <div class="card-body">
                    <p class="text-muted">Database penjahit dan karyawan koperasi.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.info("Fitur ini akan segera diaktifkan setelah data diupload.")

    elif selected == "Penjualan":
        # Placeholder untuk halaman Penjualan
        st.markdown("""
            <div class="white-card">
                <div style="background-color: #f1f5f9; padding: 15px 20px; border-bottom: 1px solid #e2e8f0;">
                    <h2 style="margin: 0; font-size: 20px; color: #064e3b;">💰 Histori Penjualan</h2>
                </div>
                <div class="card-body">
                    <p class="text-muted">Rekapitulasi proyek dan transaksi penjualan.</p>
                </div>
            </div>
        """, unsafe_allow_html=True)
        st.info("Fitur ini akan segera diaktifkan setelah data diupload.")

if __name__ == "__main__":
    main()