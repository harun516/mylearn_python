import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

# Membaca data dari file CSV
data_statistik = pd.read_csv('disdukcapil-2-od_17892_jml_penduduk__jk_kabupatenkota_data.csv')

# Memilih kolom yang akan digunakan sebagai fitur (X) dan target (y)
X = data_statistik['nama_kabupaten_kota']  # Ganti dengan kolom yang sesuai
y = data_statistik['jumlah_penduduk']  # Ganti dengan kolom yang sesuai

# Membagi data menjadi data latih dan data uji
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Membuat pipeline dengan TF-IDF dan Linear Regression
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('regressor', LinearRegression())
])

# Melatih model
model.fit(X_train, y_train)

# Prediksi jumlah penduduk untuk data uji
y_pred = model.predict(X_test)

# Evaluasi performa model menggunakan Mean Squared Error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Input kata kunci dari pengguna
kata_kunci_input = input("Masukkan kata kunci : ")
tahun_input = int(input("Masukkan tahun: "))

# Filter data berdasarkan kata kunci dan tahun
data_pertanyaan = data_statistik[data_statistik['nama_kabupaten_kota'].str.contains(kata_kunci_input, case=False) & (data_statistik['tahun'] == tahun_input)]

# Jika data ditemukan, tampilkan data
if not data_pertanyaan.empty:
    print("Hasil:")
    for index, row in data_pertanyaan.iterrows():
        print(f"{row['nama_kabupaten_kota']} {row['jumlah_penduduk']}")
    total_penduduk = data_pertanyaan['jumlah_penduduk'].sum()
    print(f"Total {total_penduduk}")
else:
    print("Data tidak ditemukan.")

# # Input pertanyaan dari pengguna
# pertanyaan_input = input("Masukkan pertanyaan (contoh: Berapa jumlah penduduk di bekasi tahun 2013): ")

# # Ekstrak kata kunci dari pertanyaan
# kata_kunci = pertanyaan_input.split()

# # Filter data berdasarkan kata kunci
# data_pertanyaan = data_statistik.copy()
# for kata in kata_kunci:
#     data_pertanyaan = data_pertanyaan[data_pertanyaan['nama_kabupaten_kota'].str.contains(kata, case=False, na=False)]

# print(data_pertanyaan)

# # Jika data ditemukan, tampilkan hasil
# if not data_pertanyaan.empty:
#     print("Hasil:")
#     for index, row in data_pertanyaan.iterrows():
#         print(f"{row['nama_kabupaten_kota']} {row['jumlah_penduduk']}")
#     total_penduduk = data_pertanyaan['jumlah_penduduk'].sum()
#     print(f"Total {total_penduduk}")
# else:
#     print("Data tidak ditemukan.")