import pandas as pd
import database as db
import os

# --- KONFIGURASI ---
nama_file_csv = "data_penjahit.csv"

# --- CEK FILE ---
if not os.path.exists(nama_file_csv):
    print(f"❌ File '{nama_file_csv}' tidak ditemukan.")
    exit()

print(f"📂 Membaca file: {nama_file_csv}")

try:
    df = pd.read_csv(nama_file_csv)
    dtype={'Kode Penjahit': str}
except Exception as e:
    print(f"❌ Gagal membaca CSV: {e}")
    exit()

print("🚀 Mulai memproses data...")

berhasil = 0
gagal = 0

# --- FUNGSI BANTUAN ---

def to_null(value):
    """Ubah NaN / string kosong jadi None (MySQL NULL)"""
    if pd.isna(value) or str(value).strip() == "":
        return None
    return str(value).strip()

def to_bool(value):
    """Konversi TRUE/FALSE dari CSV ke Boolean"""
    if pd.isna(value):
        return None
    val = str(value).strip().lower()
    if val in ["true", "1", "ya", "yes"]:
        return True
    if val in ["false", "0", "tidak", "no"]:
        return False
    return None  # kalau tidak jelas

def to_int(value):
    if pd.isna(value) or str(value).strip() == "":
        return None
    try:
        return int(value)
    except:
        return None

# --- LOOP DATA ---
for index, row in df.iterrows():
    try:
        kode_penjahit = to_null(row['Kode Penjahit'])
        nama          = to_null(row['Nama'])
        nik           = to_null(row['NIK'])
        alamat        = to_null(row['Alamat'])
        kecamatan     = to_null(row['Kecamatan'])
        usia          = to_int(row['Usia'])

        kerapian        = to_bool(row['Kerapian'])
        ketepatan_waktu = to_bool(row['Ketepatan Waktu'])
        quantity        = to_bool(row['Quantity'])
        komitmen        = to_bool(row['Komitmen'])

        spesialis = to_null(row['Spesialis'])
        status_km = to_null(row['Status Keluarga Miskin'])

        sukses = db.insert_penjahit(
            kode_penjahit,
            nama,
            nik,
            alamat,
            kecamatan,
            usia,
            kerapian,
            ketepatan_waktu,
            quantity,
            komitmen,
            spesialis,
            status_km
        )

        if sukses:
            berhasil += 1
        else:
            gagal += 1

    except Exception as e:
        print(f"⚠️ Error baris {index}: {e}")
        gagal += 1

print("-" * 40)
print(f"🎉 Selesai! Berhasil: {berhasil}, Gagal: {gagal}")
