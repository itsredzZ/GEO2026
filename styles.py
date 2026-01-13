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

    /* DATAFRAME / TABLE STYLING */
    /* Force table background to be white and text black */
    div[data-testid="stDataFrame"] {
        background-color: #ffffff !important;
        border: 1px solid #e2e8f0;
        border-radius: 8px;
        padding: 10px;
    }
    
    div[data-testid="stDataFrame"] div[role="grid"] {
        color: #334155 !important; /* Dark Grey Text */
        background-color: #ffffff !important;
    }
    
    /* Header Table */
    div[data-testid="stDataFrame"] div[role="columnheader"] {
        background-color: #f8fafc !important;
        color: #0f172a !important;
        font-weight: 600 !important;
    }

    /* CARD STYLING */
    .white-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        margin-bottom: 20px;
        border: 1px solid #e2e8f0;
    }
    </style>
    """, unsafe_allow_html=True)