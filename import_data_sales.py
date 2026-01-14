import pandas as pd
import database as db
import os

# --- KONFIGURASI ---
nama_file_csv = "Total quantity monthly.csv"

# --- CEK FILE ---
if not os.path.exists(nama_file_csv):
    print(f"❌ File '{nama_file_csv}' tidak ditemukan.")
    exit()

print(f"📂 Membaca file: {nama_file_csv}")

try:
    df = pd.read_csv(nama_file_csv)
except Exception as e:
    print(f"❌ Gagal membaca CSV: {e}")
    exit()

print("🚀 Mulai memproses data...")

berhasil = 0
gagal = 0

# --- FUNGSI BANTUAN ---
def to_int(value):
    if pd.isna(value) or str(value).strip() == "":
        return None
    try:
        return int(value)
    except:
        return None

def to_str(value):
    if pd.isna(value) or str(value).strip() == "":
        return None
    return str(value).strip()

# --- LOOP DATA ---
for index, row in df.iterrows():
    try:
        year        = to_int(row['YEAR'])
        month       = to_int(row['MONTH'])
        month_name  = to_str(row['TANGGAL PEMESANAN - Month'])
        item_count  = to_int(row['COUNTA of ITEM PROJECT'])
        total_qty   = to_int(row['SUM of QTY'])

        sukses = db.insert_sales_monthly(
            year,
            month,
            month_name,
            item_count,
            total_qty
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
