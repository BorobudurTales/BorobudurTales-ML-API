# 🛕 FastAPI BorobudurTales 

Aplikasi backend berbasis **FastAPI** untuk klasifikasi relief Karmawibhangga menggunakan model machine learning dan menampilkan narasi berdasarkan hasil klasifikasi. Proyek ini mendukung pengunggahan gambar, prediksi otomatis, serta penyajian narasi deskriptif dari file CSV.

---

## 🚀 Demo Online

🔗 **Coba langsung di Hugging Face Spaces**:  
👉 [https://huggingface.co/spaces/solihin0212/Borobudur-Tales](https://solihin0212-borobudur-tales-5394554.hf.space))


---

## 📂 Struktur Folder

```
.
├── model/                         # Berisi model ML (.h5)
├── Dockerfile                     # Konfigurasi Docker
├── app.py                         # File utama FastAPI
├── narasi-karmawibhangga.csv     # Narasi untuk setiap kelas/kategori
├── requirements.txt              # Daftar dependensi Python
├── README.md                      # Dokumentasi proyek ini
```

---

## 🚀 Fitur Utama

- ✅ Upload gambar untuk diklasifikasi secara otomatis
- 🧠 Model machine learning (CNN atau lainnya) untuk mengenali relief
- 📜 Narasi deskriptif dari file CSV berdasarkan hasil klasifikasi
- 🌐 API dokumentasi otomatis dengan Swagger UI
- 🐳 Dukungan containerization dengan Docker

---

## 🔧 Instalasi dan Menjalankan Aplikasi

### 1. Clone Repository
```bash
git clone https://github.com/BorobudurTales/BorobudurTales-ML-API.git
cd BorobudurTales-ML-API
```

### 2. Aktifkan Virtual Environment (opsional tapi disarankan)

#### Windows
```bash
python -m venv .venv
.venv\Scripts\activate
```

#### macOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependensi
```bash
pip install -r requirements.txt
```

### 4. Jalankan Aplikasi FastAPI
```bash
uvicorn app:app --reload
```

---

## 🌐 Dokumentasi API

Setelah menjalankan server, buka di browser:

- Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🧪 Contoh Endpoint

### 🔍 `POST /predict`

#### Deskripsi:
Melakukan klasifikasi gambar dan mengembalikan label beserta narasi.

#### Form Data:
- `image`: file gambar `.jpg` atau `.png`

#### Response (Contoh):
```json
{
  "filename": "001-Killing-Living-Beings-Original.jpg",
  "similarity": 0.9406542778015137,
  "tema": "Pembunuhan",
  "narasi": "Di sebuah desa nelayan, sekelompok orang tengah bersuka cita. Para nelayan sibuk menyiapkan jebakan mereka di laut, berharap hasil tangkapan yang melimpah. Di sisi lain, para pemusik memainkan alat musik dengan riang, seolah mendukung kegiatan itu sebagai sebuah hiburan. Seorang tokoh terkemuka berdiri memuji para nelayan, menyebutnya sebagai kerja keras yang patut diapresiasi. Di tengah keramaian itu, seseorang membawa hasil tangkapan dengan bangga, menunjukkan keberhasilan mereka hari itu. Namun, di balik suasana yang tampak penuh kegembiraan, tersembunyi kenyataan bahwa makhluk-makhluk hidup telah kehilangan nyawa demi kepuasan manusia. Mereka tidak menyadari bahwa turut bersenang-senang dalam pembunuhan, bahkan hanya sebagai penonton, tetap meninggalkan jejak karma. Relief ini tidak menunjukkan akibatnya secara langsung, tetapi dalam ajaran Buddha, membunuh makhluk hidup, sekecil apa pun, membawa akibat yang berat. Bahkan rasa senang atas penderitaan makhluk lain bisa menanam benih penderitaan di masa depan. Kebahagiaan sesaat yang dibangun di atas penderitaan makhluk lain bukanlah kebahagiaan sejati.",
  "makna_moral": "Hidup yang baik bukan hanya tentang tidak menyakiti, tapi juga tentang memilih untuk tidak bersukacita atas penderitaan makhluk lain."
}
```

## 🧠 Model Machine Learning

Model yang digunakan telah dilatih sebelumnya dan disimpan dalam folder `model/`. Model ini melakukan ekstraksi fitur dan klasifikasi menggunakan pendekatan berbasis deep learning (misalnya `ResNet`, `MobileNet`, dsb).

---

## 📜 Dataset Narasi

File `narasi-karmawibhangga.csv` berisi deskripsi narasi sesuai label hasil klasifikasi. File ini dimuat saat startup dan digunakan untuk mencocokkan hasil prediksi.

---
