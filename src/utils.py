import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def generate_synthetic_data(n_samples=500, random_state=42):
    np.random.seed(random_state)
    jam_tidur = np.random.uniform(4, 9, n_samples)
    jam_belajar = np.random.uniform(1, 8, n_samples)
    skala_tekanan = np.random.randint(1, 6, n_samples)
    waktu_luang = np.random.uniform(0.5, 5, n_samples)
    organisasi = np.random.choice([0, 1], size=n_samples, p=[0.6, 0.4])
    
    df = pd.DataFrame({
        'jam_tidur': jam_tidur,
        'jam_belajar': jam_belajar,
        'skala_tekanan': skala_tekanan,
        'waktu_luang': waktu_luang,
        'organisasi': organisasi
    })
    
    skor_risiko = (8 - df['jam_tidur']) * 1.5 + (df['jam_belajar'] * 1.2) + (df['skala_tekanan'] * 2) - (df['waktu_luang'] * 1.3) + (df['organisasi'] * 1.0)
    df['burnout'] = (skor_risiko > skor_risiko.median()).astype(int)
    return df

def preprocess_features(X_train, X_test):
    scaler = StandardScaler()
    num_cols = ['jam_tidur', 'jam_belajar', 'skala_tekanan', 'waktu_luang']
    X_train_scaled = X_train.copy()
    X_test_scaled = X_test.copy()
    X_train_scaled[num_cols] = scaler.fit_transform(X_train[num_cols])
    X_test_scaled[num_cols] = scaler.transform(X_test[num_cols])
    return X_train_scaled, X_test_scaled, scaler
