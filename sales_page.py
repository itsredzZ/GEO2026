import streamlit as st
import database as db

def show():
    st.title("📊 Penjualan")

    st.markdown('<div class="white-card">', unsafe_allow_html=True)
    st.subheader("Ringkasan Penjualan Bulanan")
    st.caption("Menampilkan total penjualan per bulan (tanpa detail item).")

    df = db.get_sales_monthly()

    if not df.empty:

        # ===== FILTER =====
        col1, col2 = st.columns(2)

        with col1:
            tahun_list = ["Semua"] + sorted(df["Tahun"].unique().tolist())
            tahun = st.selectbox("📅 Tahun", tahun_list)

        with col2:
            bulan_list = ["Semua"] + df["Bulan"].unique().tolist()
            bulan = st.selectbox("🗓️ Bulan", bulan_list)

        # Apply filter
        if tahun != "Semua":
            df = df[df["Tahun"] == tahun]

        if bulan != "Semua":
            df = df[df["Bulan"] == bulan]

        # ===== TABEL =====
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            height=450,
            column_config={
                "Total Qty": st.column_config.NumberColumn(
                    "Total Qty",
                    help="Total barang terjual dalam bulan tersebut",
                    format="%d"
                ),
                "Jumlah Item": st.column_config.NumberColumn(
                    "Jumlah Item",
                    help="Jumlah jenis item yang terjual",
                    format="%d"
                )
            }
        )

    else:
        st.info("Belum ada data penjualan.")

    st.markdown('</div>', unsafe_allow_html=True)
