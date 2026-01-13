import mysql.connector
import pandas as pd

def get_db_connection():
    try:
        return mysql.connector.connect(
            host="localhost", user="root", password="", database="db_inventory"
        )
    except mysql.connector.Error:
        return None

def load_data():
    conn = get_db_connection()
    if conn:
        df = pd.read_sql("SELECT * FROM stok_barang ORDER BY id DESC", conn)
        conn.close()
        return df
    return pd.DataFrame()

def insert_data(tgl, spl, itm, qty, hrg, ket):
    conn = get_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO stok_barang (tanggal_pembelian,supplier,item,quantity,harga,keterangan) VALUES (%s,%s,%s,%s,%s,%s)", (tgl, spl, itm, qty, hrg, ket))
        conn.commit()
        conn.close()
        return True
    return False

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