import streamlit as st

def load_css():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* 1. BACKGROUND UTAMA (ABU-ABU MUDA) */
    /* Ini yang membuat layar tidak putih semua */
    .stApp { 
        font-family: 'Inter', sans-serif;
        background-color: #f3f4f6 !important; /* Abu-abu Dashboard */
        color: #064e3b !important; /* Teks tetap Hijau Tua */
    }
    
    /* 2. SIDEBAR (Tetap Hijau Muda seperti Navbar Koperasi) */
    section[data-testid="stSidebar"] {
        background-color: #d1fae5 !important; 
        border-right: 1px solid #6ee7b7;
    }
    
    div[data-testid="stSidebarUserContent"] {
        background-color: #d1fae5 !important;
    }

    /* 3. INPUT FIELDS (Agar tetap bersih) */
    input, .stTextInput, .stNumberInput, .stDateInput, .stTextArea {
        color: #064e3b !important; 
    }
    
    div[data-baseweb="input"], div[data-baseweb="select"] {
        background-color: #ffffff !important; 
        border: 1px solid #bbf7d0 !important;
        color: #064e3b !important;
    }
    
    div[role="listbox"] ul { background-color: #ffffff !important; }
    
    /* 4. KARTU (CARD) - TETAP PUTIH AGAR KONTRAS */
    .white-card {
        background-color: #ffffff;
        border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
        /* Hapus padding global agar header bisa full width */
        padding: 0px !important; 
        overflow: hidden; /* Agar warna header tidak keluar dari sudut membulat */
    }
    
    /* Tambahkan class baru untuk isi kartu agar tetap rapi */
    .card-body {
        padding: 20px;
        color: #064e3b;
    }
    
    .card-title {
        font-size: 16px;
        font-weight: 600;
        color: #059669;
        margin-bottom: 15px;
    }

    /* 5. HEADER FORM */
    .form-header {
        background-color: #ecfdf5;
        padding: 10px 15px;
        border-bottom: 1px solid #bbf7d0;
        border-radius: 12px 12px 0 0;
        font-weight: 600;
        color: #064e3b;
    }
    
    /* 6. METRIC BOX */
    [data-testid="stMetric"] {
        background-color: #ffffff !important;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e2e8f0; /* Border abu tipis */
        box-shadow: 0 1px 2px rgba(0,0,0,0.05);
    }
    
    [data-testid="stMetricLabel"] { color: #059669 !important; } 
    [data-testid="stMetricValue"] { color: #064e3b !important; }
    
    /* 7. TABEL */
    [data-testid="stDataFrame"] {
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        background-color: white !important;
    }
    
    header[data-testid="stHeader"] { background-color: rgba(0,0,0,0); }
    
    ::-webkit-scrollbar { width: 10px; background: #f3f4f6; }
    ::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 5px; }
    </style>
""", unsafe_allow_html=True)