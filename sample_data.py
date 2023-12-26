import pandas as pd

# Ganti 'nama_file.csv' dengan nama file CSV yang sesuai
file_path = 'disdukcapil-2-od_17892_jml_penduduk__jk_kabupatenkota_data.csv'

# Gunakan fungsi read_csv() untuk membaca data dari file CSV
df = pd.read_csv(file_path)

# Mengelompokkan berdasarkan Kota/Kabupaten dan menghitung total penduduk
total_penduduk_per_kota = df.groupby('nama_kabupaten_kota')['jumlah_penduduk'].sum()

# Mengurutkan berdasarkan Jumlah Penduduk secara descending
total_penduduk_per_kota = total_penduduk_per_kota.sort_values(ascending=False)

# Menampilkan kota/kabupaten dengan jumlah penduduk terbanyak (misalnya, 5 teratas)
print(total_penduduk_per_kota.head())