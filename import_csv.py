import pandas as pd
import database as db 
import os
import re
from datetime import date

# --- KONFIGURASI ---
nama_file_csv = "Dataset - Supplier and stocks - project recap 2025 (cleaned).csv"

# --- CEK FILE ---
if not os.path.exists(nama_file_csv):
    print(f"❌ Error: File '{nama_file_csv}' tidak ditemukan.")
    exit()

print(f"📂 Membaca file: {nama_file_csv} ...")

try:
    df = pd.read_csv(nama_file_csv)
    # Forward Fill untuk mengisi data kosong bekas Merge
    df = df.ffill()
except Exception as e:
    print(f"❌ Gagal membaca CSV. Error: {e}")
    exit()

print("🚀 Mulai memproses data...")

berhasil = 0
gagal = 0

# --- FUNGSI MEMBERSIHKAN HARGA ---
def clean_currency(value):
    if isinstance(value, str):
        clean_str = re.sub(r'[Rp\s,.]', '', value, flags=re.IGNORECASE)
        return int(clean_str) if clean_str.isdigit() else 0
    return value

for index, row in df.iterrows():
    try:
        # --- 1. LOGIKA TANGGAL BARU (Bulan 1-12 menjadi Tanggal Lengkap) ---
        raw_bulan = row['TANGGAL\nPEMESANAN']
        
        try:
            # Ambil angka bulannya (misal: 1, 2, ..., 12)
            bulan = int(float(raw_bulan)) 
            tahun = 2025 # Kita kunci tahun 2025 sesuai nama file
            
            # Validasi: Pastikan angkanya 1-12
            if 1 <= bulan <= 12:
                # Kita ubah jadi: 2025-{bulan}-01
                tgl = date(tahun, bulan, 1) 
            else:
                # Jika angkanya aneh (misal 13), pakai tanggal hari ini
                tgl = date.today()
        except:
            # Jika data kosong/error, pakai tanggal hari ini
            tgl = date.today()

        # --- 2. MAPPING DATA LAIN ---
        spl = row['INSTANSI']      
        itm = row['ITEM PROJECT']  
        qty = row['QTY']           
        
        # Bersihkan Harga
        hrg_raw = row['HARGA']
        hrg = clean_currency(hrg_raw)
        
        # Keterangan
        ket = row['SERAGAM SEKOLAH']

        # --- 3. INSERT KE DATABASE ---
        sukses = db.insert_data(tgl, spl, itm, qty, hrg, ket)
        
        if sukses:
            berhasil += 1
        else:
            gagal += 1
            print(f"⚠️ Gagal insert baris {index+2}")

    except KeyError as e:
        print(f"❌ Error Kolom Tidak Ditemukan: {e}")
        break
    except Exception as e:
        print(f"⚠️ Error baris {index+2}: {e}")
        gagal += 1

print("-" * 30)
print(f"🎉 Selesai! Berhasil: {berhasil}, Gagal: {gagal}")