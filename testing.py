import pandas as pd

# Baca dataset (pastikan dataset sudah dinormalisasi)
file_path = 'disdukcapil-2-od_17892_jml_penduduk__jk_kabupatenkota_data.csv'
df = pd.read_csv(file_path)

# Fungsi pencarian data berdasarkan nama_kabupaten_kota
def cari_data_kabupaten(df, nama_kabupaten):
    hasil_pencarian = df[df['nama_kabupaten_kota'] == nama_kabupaten]
    return hasil_pencarian[['nama_kabupaten_kota', 'jumlah_penduduk']]

# Contoh penggunaan
nama_kabupaten_input = input('Nama_Kabupaten_Anda')
hasil_pencarian = cari_data_kabupaten(df, nama_kabupaten_input)

# Menampilkan hasil pencarian
print(hasil_pencarian)
