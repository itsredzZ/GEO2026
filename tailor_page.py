import streamlit as st
import pandas as pd
import database as db


def show():
    st.title("👷 Data Karyawan")

    st.markdown('<div class="white-card">', unsafe_allow_html=True)
    st.subheader("Daftar Karyawan / Penjahit")
    st.caption("Menampilkan data karyawan dari database (read-only).")

    df = db.get_all_karyawan()

    if not df.empty:
        # --- SEARCH ---
        search = st.text_input(
            "🔍 Cari Karyawan:",
            placeholder="Nama / Kode Penjahit / Kecamatan"
        )

        if search:
            df = df[
                df["Nama"].str.contains(search, case=False, na=False)
                | df["Kode Penjahit"].str.contains(search, case=False, na=False)
                | df["Kecamatan"].str.contains(search, case=False, na=False)
            ]

        # --- TABEL ---
        st.dataframe(
            df,
            use_container_width=True,
            hide_index=True,
            height=520,
            column_config={
                "Usia": st.column_config.NumberColumn(
                    "Usia", format="%d th"
                ),
                "Kerapian": st.column_config.CheckboxColumn("Rapi"),
                "Ketepatan Waktu": st.column_config.CheckboxColumn("Tepat Waktu"),
                "Quantity": st.column_config.CheckboxColumn("Quantity OK"),
                "Komitmen": st.column_config.CheckboxColumn("Komitmen")
            }
        )
    else:
        st.info("Belum ada data karyawan.")

    st.markdown('</div>', unsafe_allow_html=True)
