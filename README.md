# 📊 Student Burnout Predictor Web Application

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Flask-black.svg)](https://flask.palletsprojects.com/)
[![Deployment](https://img.shields.io/badge/deployed-Vercel-000000.svg?logo=vercel)](https://vercel.com/)
[![License](https://img.shields.io/badge/license-Proprietary-red.svg)](#-lisensi)

Aplikasi berbasis web modern yang berfungsi sebagai *Early Warning System* (Sistem Deteksi Dini) untuk mengukur dan memetakan risiko kejenuhan akademis (*academic burnout*) pada mahasiswa. Sistem ini mengintegrasikan pendekatan kuantitatif (durasi aktivitas harian) dengan pendekatan kualitatif psikometri standardisasi **Oldenburg Burnout Inventory (OLBI)** menggunakan model *Machine Learning*.

🚀 **Link Aplikasi Live:** [burnout-predictor-j795.vercel.app](https://burnout-predictor-j795.vercel.app)

---

## ✨ Fitur Utama
* **Premium Dashboard UI:** Antarmuka mewah berbasis *Glassmorphism* menggunakan Tailwind CSS.
* **Dual Theme Support:** Mendukung Mode Gelap (Dark Mode), Terang (Light Mode), dan Otomatis mengikuti preferensi sistem perangkat.
* **Machine Learning Engine:** Prediksi probabilitas risiko riil secara instan menggunakan algoritma *Logistic Regression*.
* **Scientific Standard:** Pertanyaan psikometri mengadopsi sub-skala ilmiah *Exhaustion* (kelelahan) dan *Disengagement* (penurunan minat) dari instrumen OLBI.
* **Micro-interactions:** Animasi transisi yang halus dan responsif menggunakan dukungan `Animate.css`.

---

## 🧠 Arsitektur & Pemodelan Data
Sistem ini memproses kombinasi fitur multi-dimensi untuk menghasilkan keputusan klasifikasi biner (**Aman** atau **Risiko Tinggi**):

1. **Fitur Kuantitatif (Durasi Fisik):** Jam Belajar Mandiri, Jam Tidur Harian, dan Waktu Luang (*Hobby Time*).
2. **Fitur Kualitatif (Psikometri):** Skor agregat indikator kelelahan fisik dan mental serta tingkat kerenggangan mahasiswa terhadap tugas akademik.
3. **Faktor Eksternal:** Pengaruh tingkat keaktifan di dalam organisasi kampus berintensitas tinggi.

### Pipeline Model:
* **Preprocessing:** Fitur numerik ditransformasikan menggunakan `StandardScaler` untuk menghilangkan bias skala rentang nilai.
* **Classification:** Pemodelan menggunakan fungsi aktivasi non-linear **Sigmoid** pada *Logistic Regression* untuk mengonversi kombinasi linear fitur menjadi persentase probabilitas $[0, 1]$.
* **Decision Boundary:** Ambang batas keputusan ditetapkan pada *Default Threshold* $0.5 \ (50\%)$.

---

## 📄 Lisensi
Hak Cipta © 2026 Akhmad Ridwan Ariyanto. Hak cipta dilindungi undang-undang.

Lihat file [LICENSE](./LICENSE) untuk informasi lebih lanjut mengenai batasan penggunaan kode ini.

## 📁 Struktur Folder Proyek
Proyek ini dibangun dengan struktur direktori modular yang rapi dan terpisah:

```text
BURNOUT-PREDICTOR/
│
├── .venv/                      # Python Virtual Environment (Diabaikan oleh Git)
├── models/                     # Tempat penyimpanan binary model hasil training
│   ├── logistic_model.pkl      # Berisi weight koefisien model Logistic Regression
│   └── scaler.pkl              # Ekspor konfigurasi StandardScaler
│
├── src/                        # Source code utama untuk pipeline data
│   ├── __pycache__/            # Python cache files
│   ├── train.py                # Script untuk melatih ulang model machine learning
│   └── utils.py                # Helper functions untuk pembersihan & pemrosesan data
│
├── templates/                  # Folder views/antarmuka website
│   └── index.html              # Interface utama aplikasi (Tailwind & Glassmorphism)
│
├── .gitignore                  # File konfigurasi pengabaian file sampah Git
├── app.py                      # Serverless Entry Point aplikasi Flask utama
├── requirements.txt            # Daftar library dependency python versi UTF-8
├── train_and_save.py           # Script eksekusi training menyeluruh
└── vercel.json                 # File konfigurasi routing deployment Vercel

## 📄 Lisensi
Hak Cipta © 2026 Akhmad Ridwan Ariyanto. Hak cipta dilindungi undang-undang.

Lihat file [LICENSE](./LICENSE) untuk informasi lebih lanjut mengenai batasan penggunaan kode ini.
