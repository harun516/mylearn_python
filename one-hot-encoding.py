from sklearn.preprocessing import OneHotEncoder
import pandas as pd

# Contoh data
data_statistik = pd.read_csv('disdukcapil-2-od_17892_jml_penduduk__jk_kabupatenkota_data.csv')

# Inisialisasi one-hot encoder
onehot_encoder = OneHotEncoder(sparse=False)

# Reshape data menjadi bentuk kolom
reshaped_data = pd.DataFrame(data_statistik, columns=['nama_kabupaten_kota'])
reshaped_data = reshaped_data.values.reshape(-1, 1)

# Fit dan transform data
onehot_encoded_data = onehot_encoder.fit_transform(reshaped_data)

print(onehot_encoded_data)
