import streamlit as st
import mysql.connector
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import date
from streamlit_option_menu import option_menu

# --- 1. CONFIG HALAMAN ---
st.set_page_config(
    page_title="Pixel Admin Inventory",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. CSS CUSTOM (TEMA PIXEL ADMIN - LIGHT) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* BACKGROUND UTAMA */
    .stApp { 
        background-color: #f3f4f6; 
        font-family: 'Inter', sans-serif;
    }
    
    /* SIDEBAR */
    [data-testid="stSidebar"] {
        background-color: #1e293b !important;
        border-right: 1px solid #334155;
    }
    
    [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h3 {
        color: white !important;
    }
            
    /* HILANGKAN PADDING ATAS */
    .block-container { padding-top: 1.5rem; }

    /* --- CARDS STYLE --- */
    .white-card {
        background-color: white;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        margin-bottom: 20px;
        border: 1px solid #f3f4f6;
    }
    
    .card-title {
        font-size: 16px;
        font-weight: 600;
        color: #111827;
        margin-bottom: 15px;
    }

    /* SPARKLINE CARDS (DASHBOARD) */
    .solid-card {
        border-radius: 12px;
        padding: 20px;
        color: white;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    }
    .bg-blue { background-color: #2563eb; }
    .bg-orange { background-color: #f97316; }
    .bg-green { background-color: #10b981; }
    
    .solid-value { font-size: 28px; font-weight: 700; margin-top: 5px; }

    /* FORM STYLE */
    .form-header {
        background-color: #f9fafb;
        padding: 10px 15px;
        border-bottom: 1px solid #e5e7eb;
        border-radius: 12px 12px 0 0;
        font-weight: 600;
        color: #374151;
    }

    h1, h2, h3 { color: #111827 !important; }
    .text-muted { color: #6b7280; font-size: 14px; }
    [data-testid="InputInstructions"] { display: none !important; }
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

# --- 4. DATA OPERATIONS (CRUD) ---
def load_data():
    conn = get_db_connection()
    if conn:
        df = pd.read_sql("SELECT * FROM stok_barang ORDER BY id DESC", conn)
        conn.close()
        return df
    return pd.DataFrame()

def update_data(id_b, tgl, spl, itm, qty, hrg, ket):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE stok_barang SET tanggal_pembelian=%s, supplier=%s, item=%s, quantity=%s, harga=%s, keterangan=%s WHERE id=%s", 
                       (tgl, spl, itm, qty, hrg, ket, id_b))
        conn.commit()
        conn.close()
        return True
    return False

def delete_data(id_b):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM stok_barang WHERE id=%s", (id_b,))
        conn.commit()
        conn.close()
        return True
    return False

# --- 5. HELPER CHART ---
def render_sparkline(data_list, color_hex):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        y=data_list, mode='lines', line=dict(color=color_hex, width=3),
        fill='tozeroy', fillcolor=f"rgba{tuple(int(color_hex.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) + (0.1,)}"
    ))
    fig.update_layout(showlegend=False, margin=dict(l=0, r=0, t=0, b=0), height=50, xaxis=dict(visible=False), yaxis=dict(visible=False), paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    return fig

# --- 6. PAGE: DASHBOARD (VIEW ONLY) ---
def show_dashboard():
    # -- HEADER BARU (Tanpa Search Bar) --
    # Kita buat 2 kolom: Kiri (Judul), Kanan (Profil Admin)
    col_header_left, col_header_right = st.columns([3, 1])
    
    with col_header_left:
        st.title("Dashboard Control")
        st.markdown('<p class="text-muted">Home > Dashboard</p>', unsafe_allow_html=True)
    
    with col_header_right:
        # Menampilkan status admin di pojok kanan agar rapi
        st.markdown("<div style='text-align:right; padding-top:20px; color:#374151;'>🔔 🇺🇸 <b>Hi, Admin</b></div>", unsafe_allow_html=True)

    st.markdown("---") # Garis pemisah tipis

    df = load_data()
    
    # Dummy Data untuk visualisasi grafik sparkline
    trend_1 = np.random.randint(10, 50, 10) 
    trend_2 = np.random.randint(20, 80, 10)
    trend_3 = np.random.randint(5, 30, 10)
    trend_4 = np.random.randint(40, 100, 10)

    if not df.empty:
        total_aset = (df['quantity'] * df['harga']).sum()
        
        # BARIS 1: Sparklines
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown(f'<div class="white-card"><div class="text-muted">Total Transaksi</div><h3 style="margin:0;">{len(df)}</h3></div>', unsafe_allow_html=True)
            st.plotly_chart(render_sparkline(trend_1, '#2563eb'), use_container_width=True, config={'displayModeBar': False})
        with col2:
            st.markdown(f'<div class="white-card"><div class="text-muted">Aset (Rp)</div><h3 style="margin:0; color:#10b981;">{total_aset/1000:,.0f}k</h3></div>', unsafe_allow_html=True)
            st.plotly_chart(render_sparkline(trend_2, '#10b981'), use_container_width=True, config={'displayModeBar': False})
        with col3:
            st.markdown(f'<div class="white-card"><div class="text-muted">Item Terjual</div><h3 style="margin:0; color:#f97316;">{df["quantity"].sum()}</h3></div>', unsafe_allow_html=True)
            st.plotly_chart(render_sparkline(trend_3, '#f97316'), use_container_width=True, config={'displayModeBar': False})
        with col4:
            st.markdown(f'<div class="white-card"><div class="text-muted">Supplier</div><h3 style="margin:0; color:#facc15;">{df["supplier"].nunique()}</h3></div>', unsafe_allow_html=True)
            st.plotly_chart(render_sparkline(trend_4, '#facc15'), use_container_width=True, config={'displayModeBar': False})

        # BARIS 2: Widgets
        c_left, c_mid, c_right = st.columns([1, 1.2, 1.2])
        with c_left:
            st.markdown(f'<div class="solid-card bg-blue"><div class="solid-title">Total Sales</div><div class="solid-value">Rp {total_aset:,.0f}</div></div>', unsafe_allow_html=True)
            st.markdown(f'<div class="solid-card bg-green"><div class="solid-title">Active Items</div><div class="solid-value">{df["item"].nunique()} Types</div></div>', unsafe_allow_html=True)
        
        with c_mid:
            st.markdown('<div class="white-card" style="height:100%;">', unsafe_allow_html=True)
            st.subheader("Top Suppliers")
            df_supp = df.groupby('supplier')['quantity'].sum().reset_index().sort_values(by='quantity', ascending=False).head(5)
            for _, row in df_supp.iterrows():
                st.markdown(f'<div style="display:flex; justify-content:space-between; padding:10px 0; border-bottom:1px solid #f3f4f6;"><span>{row["supplier"]}</span><span style="color:#2563eb; font-weight:bold; background:#eff6ff; padding:2px 8px; border-radius:10px;">{row["quantity"]}</span></div>', unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

        with c_right:
             st.markdown('<div class="white-card" style="padding:0; overflow:hidden; height:100%;"><img src="https://images.unsplash.com/photo-1586528116311-ad8dd3c8310d?ixlib=rb-4.0.3&auto=format&fit=crop&w=800&q=80" style="width:100%; height:200px; object-fit:cover;"><div style="padding:20px;"><h4>Logistics Update</h4><p class="text-muted">Check the latest shipping routes.</p></div></div>', unsafe_allow_html=True)
    else:
        st.info("Data Kosong")

# --- 7. PAGE: SUPPLIER MANAGEMENT (DETAIL & CRUD) ---
def show_supplier_page():
    # Header Sederhana
    st.title("Supplier Management")
    st.markdown('<p class="text-muted">Home > Supplier (Full Access)</p>', unsafe_allow_html=True)
    
    df = load_data()
    if df.empty:
        st.warning("Belum ada data.")
        return

    # --- BAGIAN 1: DETAIL DIAGRAM (ANALYTICS) ---
    st.markdown("### 📊 Supplier Analytics")
    row1_1, row1_2 = st.columns(2)
    
    with row1_1:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Total Spending per Supplier</div>', unsafe_allow_html=True)
        df['total_belanja'] = df['quantity'] * df['harga']
        df_spend = df.groupby('supplier')['total_belanja'].sum().reset_index().sort_values(by='total_belanja', ascending=True)
        
        fig_bar = px.bar(df_spend, x='total_belanja', y='supplier', orientation='h', text_auto='.2s',
                         color_discrete_sequence=['#2563eb'])
        fig_bar.update_layout(height=300, margin=dict(l=0, r=0, t=0, b=0), plot_bgcolor='white')
        st.plotly_chart(fig_bar, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    with row1_2:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">Frequency of Purchase</div>', unsafe_allow_html=True)
        df_freq = df['supplier'].value_counts().reset_index()
        df_freq.columns = ['supplier', 'count']
        
        fig_donut = px.pie(df_freq, names='supplier', values='count', hole=0.6,
                           color_discrete_sequence=px.colors.sequential.Bluyl)
        fig_donut.update_layout(height=300, margin=dict(l=0, r=0, t=0, b=0))
        st.plotly_chart(fig_donut, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    # --- BAGIAN 2: TABEL DATA & CRUD ACTION ---
    st.markdown("### 🛠️ Data Management")
    
    col_table, col_edit = st.columns([2, 1])
    
    # KOLOM KIRI: TABEL
    with col_table:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">List of All Transactions</div>', unsafe_allow_html=True)
        
        st.dataframe(
            df,
            column_config={
                "id": st.column_config.NumberColumn("ID", width="small"),
                "tanggal_pembelian": "Date",
                "harga": st.column_config.NumberColumn("Price", format="Rp %d"),
                "quantity": st.column_config.NumberColumn("Qty"),
                "total_belanja": st.column_config.NumberColumn("Total", format="Rp %d")
            },
            use_container_width=True,
            hide_index=True,
            height=450
        )
        st.markdown('</div>', unsafe_allow_html=True)

    # KOLOM KANAN: FORM EDIT/DELETE
    with col_edit:
        st.markdown('<div class="white-card" style="padding:0;">', unsafe_allow_html=True)
        st.markdown('<div class="form-header">✏️ Edit / Delete Action</div>', unsafe_allow_html=True)
        
        st.markdown('<div style="padding:20px;">', unsafe_allow_html=True)
        
        # Selectbox ID
        list_id = df['id'].tolist()
        pilih_id = st.selectbox("Select ID to Action:", list_id)
        
        if pilih_id:
            curr_data = df[df['id'] == pilih_id].iloc[0]
            
            with st.form("edit_form"):
                st.caption(f"Editing Transaction ID: {pilih_id}")
                e_tgl = st.date_input("Date", pd.to_datetime(curr_data['tanggal_pembelian']))
                e_spl = st.text_input("Supplier Name", curr_data['supplier'])
                e_itm = st.text_input("Item Name", curr_data['item'])
                e_qty = st.number_input("Quantity", value=int(curr_data['quantity']))
                e_hrg = st.number_input("Price (Rp)", value=int(curr_data['harga']))
                e_ket = st.text_area("Notes", curr_data['keterangan'])
                
                st.markdown("---")
                c_btn1, c_btn2 = st.columns(2)
                
                # Tombol Update
                if c_btn1.form_submit_button("💾 Save", type="primary", use_container_width=True):
                    if update_data(pilih_id, e_tgl, e_spl, e_itm, e_qty, e_hrg, e_ket):
                        st.success("Updated!")
                        st.rerun()
                
                # Tombol Delete
                if c_btn2.form_submit_button("🗑️ Delete", type="secondary", use_container_width=True):
                    if delete_data(pilih_id):
                        st.success("Deleted!")
                        st.rerun()

        st.markdown('</div></div>', unsafe_allow_html=True)

# --- 8. GLOBAL MODAL INPUT ---
@st.dialog("➕ Add New Transaction")
def input_modal():
    with st.form("add_transaction"):
        c1, c2 = st.columns(2)
        tgl = c1.date_input("Date", date.today())
        spl = c1.text_input("Supplier Name", placeholder="e.g. PT Jaya Abadi")
        itm = c2.text_input("Item Name", placeholder="e.g. Laptop ASUS")
        qty = c1.number_input("Quantity", 1)
        hrg = c2.number_input("Price", 0, step=1000)
        ket = st.text_input("Notes")
        
        if st.form_submit_button("Submit Data", type="primary", use_container_width=True):
            conn = get_db_connection()
            if conn:
                cur = conn.cursor()
                cur.execute("INSERT INTO stok_barang (tanggal_pembelian,supplier,item,quantity,harga,keterangan) VALUES (%s,%s,%s,%s,%s,%s)", (tgl, spl, itm, qty, hrg, ket))
                conn.commit()
                conn.close()
                st.success("Data Added!")
                st.rerun()

# --- 9. MAIN APP ---
def main():
    with st.sidebar:
        st.markdown("""
        <div style="display:flex; align-items:center; margin-bottom:20px;">
            <div style="width:30px; height:30px; background:linear-gradient(45deg, #2563eb, #ec4899); border-radius:5px; margin-right:10px;"></div>
            <h3 style="margin:0; font-weight:700;">StockAD</h3>
        </div>
        """, unsafe_allow_html=True)
        
        selected = option_menu(
            menu_title=None,
            options=["Dashboard", "Supplier", "Settings"],
            icons=["house", "truck", "gear"], 
            default_index=0,
            styles={
                "container": {"background-color": "#1e293b", "padding": "0!important"},
                "icon": {"color": "#6b7280", "font-size": "16px"}, 
                "nav-link": {"font-size": "15px", "text-align": "left", "margin":"5px", "color": "#4b5563"},
                "nav-link-selected": {"background-color": "#eff6ff", "color": "#2563eb", "font-weight":"600"},
            }
        )
        
        st.markdown("---")
        if st.button("New Data", type="primary", use_container_width=True):
            input_modal()

    # ROUTING
    if selected == "Dashboard":
        show_dashboard()
    elif selected == "Supplier":
        show_supplier_page()
    elif selected == "Settings":
        st.title("Settings")
        st.info("Configuration page placeholder.")

if __name__ == "__main__":
    main()