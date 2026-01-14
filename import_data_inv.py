import pandas as pd
import database as db 
import os
import re

# --- KONFIGURASI ---
nama_file_csv = "Dataset - Supplier and stocks - data supplier 2025 (cleaned).csv"

# --- CEK FILE ---
if not os.path.exists(nama_file_csv):
    print(f"❌ Error: File '{nama_file_csv}' tidak ditemukan.")
    exit()

print(f"📂 Membaca file: {nama_file_csv} ...")

try:
    df = pd.read_csv(nama_file_csv)
except Exception as e:
    print(f"❌ Gagal membaca CSV. Error: {e}")
    exit()

print("🚀 Mulai memproses data...")

berhasil = 0
gagal = 0

# --- FUNGSI MEMBERSIHKAN HARGA ---
def clean_currency(value):
    if isinstance(value, str):
        # Hapus "Rp", spasi, koma, titik
        clean_str = re.sub(r'[Rp\s,.]', '', value, flags=re.IGNORECASE)
        # Jika CSV pakai koma sebagai pemisah ribuan (e.g. 19,500), hapus koma
        # Tapi hati-hati jika koma adalah desimal. 
        # Berdasarkan file Anda "19,500" -> 19500
        clean_str = value.replace(",", "").replace(".", "").replace("Rp", "").strip()
        return int(clean_str) if clean_str.isdigit() else 0
    return value

for index, row in df.iterrows():
    try:
        # --- 1. PARSING TANGGAL (DD/MM/YYYY) ---
        raw_tgl = row['TANGGAL PEMBELIAN']
        try:
            # Ubah string "22/12/2025" menjadi object date MySQL
            tgl = pd.to_datetime(raw_tgl, dayfirst=True).date()
        except:
            tgl = None
            print(f"⚠️ Format tanggal salah baris {index}: {raw_tgl}")

        # --- 2. MAPPING KOLOM CSV -> DB ---
        spl = row['NAMA SUPPLIER & PENYEDIA JASA']
        kat = row['KATEGORI ITEM']
        itm = row['ITEM']
        qty = row['QTY']
        sat = row['SATUAN']
        
        # Bersihkan Harga
        hrg = clean_currency(row['HARGA'])

        # --- 3. INSERT KE DATABASE ---
        if tgl:
            sukses = db.insert_data(tgl, spl, kat, itm, qty, sat, hrg)
            if sukses:
                berhasil += 1
            else:
                gagal += 1
        else:
            gagal += 1

    except Exception as e:
        print(f"⚠️ Error baris {index}: {e}")
        gagal += 1

print("-" * 30)
print(f"🎉 Selesai! Berhasil: {berhasil}, Gagal: {gagal}")