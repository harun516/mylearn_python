import pandas as pd
import numpy as np
from scipy.stats import zscore

# Contoh data search queries (berdasarkan frekuensi)
search_queries = [10, 12, 14, 16, 18, 20, 22, 24, 26, 100]

# Konversi ke DataFrame
df = pd.DataFrame(search_queries, columns=['search_count'])

# Hitung skor Z untuk setiap nilai
df['z_score'] = np.abs(zscore(df['search_count']))

# Tentukan batas ambang untuk anomali (contoh: z-score > 2)
anomaly_threshold = 2

# Filter data untuk mendapatkan anomali
anomalies = df[df['z_score'] > anomaly_threshold]

# Tampilkan hasil
print("Data Asli:")
print(df)
print("\nAnomali:")
print(anomalies)
