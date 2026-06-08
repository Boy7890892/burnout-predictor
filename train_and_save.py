import pickle
import os
from sklearn.model_selection import train_test_split
from src.utils import generate_synthetic_data, preprocess_features
from src.train import train_logistic_regression

def main():
    print("Mempersiapkan data dan melatih model...")
    df = generate_synthetic_data(n_samples=1000) # Perbanyak sampel agar makin kokoh
    
    X = df.drop(columns=['burnout'])
    y = df['burnout']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    X_train_scaled, X_test_scaled, scaler = preprocess_features(X_train, X_test)
    
    # Latih model
    model = train_logistic_regression(X_train_scaled, y_train)
    
    # Simpan model dan scaler ke dalam file binary (.pkl)
    os.makedirs('models', exist_ok=True)
    with open('models/logistic_model.pkl', 'wb') as f:
        pickle.dump(model, f)
    with open('models/scaler.pkl', 'wb') as f:
        pickle.dump(scaler, f)
        
    print("✅ Model dan Scaler berhasil disimpan di folder 'models/'!")

if __name__ == "__main__":
    main()