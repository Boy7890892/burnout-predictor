from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load model dan scaler yang sudah disimpan
with open('models/logistic_model.pkl', 'rb') as f:
    model = pickle.load(f)
with open('models/scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # A. Ambil data durasi riil (Kuantitatif) dari Bagian 1
        jam_tidur = float(request.form['jam_tidur'])
        jam_belajar = float(request.form['jam_belajar'])
        waktu_luang = float(request.form['waktu_luang'])
        organisasi = int(request.form['organisasi'])
        
        # B. Ambil data skala psikometri dari Bagian 2
        exhaustion = int(request.form['exhaustion'])
        disengagement = int(request.form['disengagement'])
        
        # C. Rumus Kombinasi: Skala tekanan dihitung dari rata-rata stres psikometri
        # (exhaustion + disengagement) / 2 menghasilkan skala 1-5 yang sangat akurat
        skala_tekanan = round((exhaustion + disengagement) / 2)
        
        # D. Susun ke DataFrame sesuai urutan asli model saat training
        input_data = pd.DataFrame([{
            'jam_tidur': jam_tidur,
            'jam_belajar': jam_belajar,
            'skala_tekanan': skala_tekanan,
            'waktu_luang': waktu_luang,
            'organisasi': organisasi
        }])
        
        # E. Definisikan kolom numerik yang butuh scaling
        num_cols = ['jam_tidur', 'jam_belajar', 'skala_tekanan', 'waktu_luang']
        
        # F. Jalankan Scaling & Prediksi Model AI
        input_data[num_cols] = scaler.transform(input_data[num_cols])
        
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1] * 100 
        
        return jsonify({
            'status': 'success',
            'burnout': int(prediction),
            'risiko_persen': round(probability, 2)
        })
        
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)