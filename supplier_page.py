import streamlit as st
import pandas as pd
import database as db

def show():
    st.title("Manajemen Gudang")
    st.markdown('<p class="text-muted">Home >📦 Manajemen Gudang</p>', unsafe_allow_html=True)
    
    df = db.load_data()
    if df.empty:
        st.warning("Belum ada data.")
        return

    col_table, col_edit = st.columns([2, 1])
    
    with col_table:
        st.markdown('<div class="white-card">', unsafe_allow_html=True)
        st.markdown('<div class="card-title">List of All Transactions</div>', unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True, hide_index=True, height=450)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_edit:
        st.markdown('<div class="white-card" style="padding:0;">', unsafe_allow_html=True)
        st.markdown('<div class="form-header">✏️ Edit / Delete Action</div>', unsafe_allow_html=True)
        st.markdown('<div style="padding:20px;">', unsafe_allow_html=True)
        
        list_id = df['id'].tolist()
        pilih_id = st.selectbox("Select ID to Action:", list_id)
        
        if pilih_id:
            curr_data = df[df['id'] == pilih_id].iloc[0]
            with st.form("edit_form"):
                e_tgl = st.date_input("Date", pd.to_datetime(curr_data['tanggal_pembelian']))
                e_spl = st.text_input("Supplier", curr_data['supplier'])
                e_itm = st.text_input("Item", curr_data['item'])
                e_qty = st.number_input("Qty", value=int(curr_data['quantity']))
                e_hrg = st.number_input("Price", value=int(curr_data['harga']))
                e_ket = st.text_area("Notes", curr_data['keterangan'])
                
                st.markdown("---")
                c_btn1, c_btn2 = st.columns(2)
                if c_btn1.form_submit_button("💾 Save", type="primary", use_container_width=True):
                    if db.update_data(pilih_id, e_tgl, e_spl, e_itm, e_qty, e_hrg, e_ket):
                        st.success("Updated!"); st.rerun()
                if c_btn2.form_submit_button("🗑️ Delete", type="secondary", use_container_width=True):
                    if db.delete_data(pilih_id):
                        st.success("Deleted!"); st.rerun()
        st.markdown('</div></div>', unsafe_allow_html=True)