import streamlit as st
import plotly.express as px
import database as db  # Import file database kita
import styles
styles.load_css()


def show():
    # -- HEADER --
    col_header_left, col_header_right = st.columns([3, 1])
    with col_header_left:
        st.title("Dashboard Control")
        st.markdown('<p class="text-muted">Home > Dashboard</p>', unsafe_allow_html=True)
    with col_header_right:
        st.markdown("<div style='text-align:right; padding-top:20px; color:#374151;'>🔔 🇺🇸 <b>Hi, Admin</b></div>", unsafe_allow_html=True)

    st.markdown("---") 

    df = db.load_data() # Panggil fungsi dari file database.py

    if not df.empty:
        total_penjahit = df['supplier'].nunique()
        total_pendapatan = (df['quantity'] * df['harga']).sum()
        produk_terjual = df['quantity'].sum()
        
        BATAS_AMAN = 10
        barang_menipis = df[df['quantity'] < BATAS_AMAN]
        jumlah_menipis = len(barang_menipis)

        # Baris Pertama
        row1_left, row1_right = st.columns(2)
        with row1_left:
            st.metric("Total Penjahit (Supplier)", f"{total_penjahit} Mitra", "Aktif Bekerja", border=True)
        with row1_right:
            st.metric("Total Pendapatan (Aset)", f"Rp {total_pendapatan:,.0f}".replace(",", "."), "+5% Bulan Ini", border=True)

        # Baris Kedua
        row2_left, row2_right = st.columns(2)
        with row2_left:
            st.metric("Produk Terjual (Stok)", f"{produk_terjual} Pcs", f"{len(df)} Transaksi", border=True)
        with row2_right:
            with row2_right:
                if jumlah_menipis > 0:
                    # HAPUS 'delta_color="inverse"'
                    # Karena ada tanda minus "-", otomatis warnanya jadi MERAH (Normal)
                    st.metric(
                        label="Alert: Supply Menipis", 
                        value=f"{jumlah_menipis} Item", 
                        delta="- Segera Restock", 
                        border=True
                    )
                else:
                    # Tanpa tanda minus, otomatis warnanya jadi HIJAU
                    st.metric(
                        label="Status Supply", 
                        value="Aman", 
                        delta="Semua stok > 10", 
                        border=True
                    )

        st.markdown("<br>", unsafe_allow_html=True)
        
        c_mid, c_right = st.columns([2, 1])
        with c_mid:
            st.markdown('<div class="white-card" style="height:100%;">', unsafe_allow_html=True)
            st.subheader("Top Suppliers Performance")
            df_supp = df.groupby('supplier')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False).head(5)
            fig = px.bar(df_supp, x='supplier', y='quantity', color='quantity', color_continuous_scale='Greens')
            
            fig.update_layout(
                height=300, 
                margin=dict(l=0,r=0,t=0,b=0),
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                
                # PENTING: Ubah warna font jadi HITAM/HIJAU TUA
                font=dict(color="#064e3b") 
            )
            st.plotly_chart(fig, use_container_width=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with c_right:
             st.markdown('<div class="white-card" style="padding:0; overflow:hidden; height:100%;"><img src="https://images.unsplash.com/photo-1556740758-90de374c12ad?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" style="width:100%; height:200px; object-fit:cover;"><div style="padding:20px;"><h4>Warehouse Status</h4><p class="text-muted">Cek kondisi fisik gudang dan jadwal pengiriman terbaru.</p></div></div>', unsafe_allow_html=True)
    else:
        st.info("Data Kosong. Silakan tambah data baru di menu sebelah kiri.")