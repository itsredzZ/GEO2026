import streamlit as st
import plotly.express as px
import pandas as pd
import database as db

def show():
    # --- HEADER ---
    col_header_left, col_header_right = st.columns([3, 1])
    with col_header_left:
        st.title("Executive Dashboard")
        st.markdown('<p class="text-muted">Overview Kinerja Koperasi & Prediksi Penjualan</p>', unsafe_allow_html=True)
    with col_header_right:
         if st.button("🔄 Refresh Data"):
            st.rerun()

    st.markdown("---") 

    # --- 1. LOAD METRICS DARI DATABASE ---
    metrics = db.get_dashboard_metrics()

    # --- 2. KPI CARDS (SUPERLATIVE STATS) ---
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        st.metric(
            label="💰 Nilai Aset Gudang",
            value=f"Rp {metrics['total_asset']:,.0f}".replace(",", "."),
            delta="Valuasi Stok Fisik",
            delta_color="off"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # === UPDATE: KARTU KE-2 (PENJUALAN 2025) ===
    with col2:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        st.metric(
            label="📦 Total Penjualan (2025)", # Label Baru
            value=f"{metrics['items_sold']:,.0f} Pcs",
            delta="Rekap Tahun Lalu", # Keterangan Baru
            delta_color="off"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    with col3:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        st.metric(
            label="👥 Kekuatan Produksi",
            value=f"{metrics['total_tailors']} Penjahit",
            delta="Mitra Aktif",
            delta_color="off"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # === UPDATE: KARTU KE-4 (TOP SUPPLIER) ===
    with col4:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        
        supp_name = metrics['top_supplier']
        # Potong nama jika terlalu panjang agar tidak merusak layout
        if len(supp_name) > 15:
            supp_name = supp_name[:12] + "..."
            
        st.metric(
            label="🏆 Mitra Utama (Supplier)",
            value=supp_name,
            delta=f"Suplai: {metrics['top_supplier_vol']:,.0f} Unit",
            delta_color="off"
        )
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # --- 3. SALES FORECAST VISUALIZATION (Updated from sales_forecast.py) ---
    st.subheader("📈 Analisa Tren Penjualan")
    
    col_hist, col_fore = st.columns(2)

    # === CHART KIRI: HISTORY (FILTERABLE BY YEAR) ===
    with col_hist:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        
        try:
            # 1. Load Data
            df_history = pd.read_excel("Total quantity monthly.xlsx")
            
            # 2. Data Cleaning
            df_history["date"] = pd.to_datetime(
                df_history["YEAR"].astype(str) + "-" + df_history["MONTH"].astype(str) + "-01"
            )
            df_history = df_history.sort_values("date")
            df_history["month_year"] = df_history["date"].dt.strftime("%b %Y")
            
            # 3. FILTER LOGIC (Tahun)
            # Ambil tahun unik dari data
            available_years = sorted(df_history['YEAR'].unique())
            
            # Buat Layout Header: Judul di Kiri, Dropdown di Kanan
            c_title, c_filter = st.columns([2, 1])
            with c_title:
                st.markdown("##### ⏪ Riwayat Penjualan")
            with c_filter:
                # Default pilih tahun terakhir (paling baru)
                selected_year = st.selectbox(
                    "Pilih Tahun", 
                    available_years, 
                    index=len(available_years)-1, 
                    key="hist_year_filter",
                    label_visibility="collapsed" # Sembunyikan label "Pilih Tahun" biar rapi
                )

            # 4. Terapkan Filter
            df_filtered = df_history[df_history['YEAR'] == selected_year]
            
            # 5. Plotly Visualization
            fig_hist = px.bar(
                df_filtered,
                x="month_year",
                y="SUM of QTY",  
                title=f"Total Sales Quantity ({selected_year})",
                color_discrete_sequence=["#64748b"] 
            )
            
            # UPDATED LAYOUT: Margin Kiri (l=50) diperbesar agar angka tidak terpotong
            fig_hist.update_layout(
                plot_bgcolor="white", 
                height=350, 
                margin=dict(l=50, r=20, t=40, b=40) 
            )
            st.plotly_chart(fig_hist, use_container_width=True)
            
        except Exception as e:
            st.warning(f"Data tidak tersedia ({e})")
            # Fallback ke data database jika Excel error
            df_db = db.get_monthly_sales_data()
            if not df_db.empty:
                st.bar_chart(df_db.set_index('month_year')['total_qty'])
        
        st.markdown('</div>', unsafe_allow_html=True)

    # === CHART KANAN: FORECAST (Next 12 Months) ===
    with col_fore:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        st.markdown("##### 🔮 Prediksi Penjualan 2026")
        
        try:
            # Load Data Forecast
            df_forecast = pd.read_excel("Future predicted data 2026.xlsx")
            
            # Data Cleaning
            df_forecast["date"] = pd.to_datetime(
                df_forecast["YEAR"].astype(str) + "-" + df_forecast["MONTH"].astype(str) + "-01"
            )
            df_forecast = df_forecast.sort_values("date")
            df_forecast["month_year"] = df_forecast["date"].dt.strftime("%b %Y")
            
            # Plotly Visualization
            fig_fore = px.bar(
                df_forecast,
                x="month_year",
                y="Prediction (SUM OF QTY)",
                title="Projected Sales Quantity 2026",
                color="Prediction (SUM OF QTY)",
                color_continuous_scale="Teal" # Warna Hijau/Teal (Masa Depan)
            )
            fig_fore.update_layout(plot_bgcolor="white", height=350, margin=dict(l=20, r=20, t=40, b=20))
            st.plotly_chart(fig_fore, use_container_width=True)
            
        except Exception as e:
            st.warning(f"File 'Future predicted data 2026.xlsx' tidak ditemukan. ({e})")
        
        st.markdown('</div>', unsafe_allow_html=True)

    # --- 4. WAREHOUSE ALERTS ---
    st.markdown("<br>", unsafe_allow_html=True)
    c_alert, c_info = st.columns([2, 1])

    with c_alert:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        st.subheader("⚠️ Low Stock Monitoring")
        
        # Ambil data stok menipis
        df_stock = db.get_stock_summary()
        if not df_stock.empty:
            df_low = df_stock[df_stock['Stok Tersedia'] < 10].sort_values(by='Stok Tersedia')
            
            if not df_low.empty:
                st.error(f"Perhatian! Ada {len(df_low)} item dengan stok kritis (< 10).")
                st.dataframe(
                    df_low,
                    use_container_width=True,
                    hide_index=True,
                    height=200,
                    column_config={
                        "Stok Tersedia": st.column_config.ProgressColumn(
                            "Level Stok",
                            format="%d",
                            min_value=0,
                            max_value=20,
                            help="Bar merah menunjukkan stok sangat rendah"
                        )
                    }
                )
            else:
                st.success("✅ Semua stok dalam kondisi aman.")
        else:
            st.info("Belum ada data stok di gudang.")
        st.markdown('</div>', unsafe_allow_html=True)

    with c_info:
        st.markdown('<div class="white-card" style="height:100%; display:flex; flex-direction:column; justify-content:center; align-items:center; text-align:center;">', unsafe_allow_html=True)
        st.markdown("### 💡 Insight")
        st.info("Prediksi penjualan meningkat signifikan di bulan **Juli 2026**. Persiapkan stok kain seragam sekolah 2 bulan sebelumnya.")
        st.markdown('</div>', unsafe_allow_html=True)