# 📂 Folder Size Analyzer
> **Visualisasi Performa Algoritma: Rekursif vs Iteratif**

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![GUI](https://img.shields.io/badge/GUI-Tkinter-green.svg)

## 📖 Deskripsi Project

**Folder Size Analyzer** adalah aplikasi desktop berbasis Python yang dirancang untuk mensimulasikan dan menganalisis kinerja dua pendekatan algoritma dalam penelusuran struktur data Tree (Sistem File):
1.  **Pendekatan Rekursif:** Menggunakan fungsi yang memanggil dirinya sendiri (standar DFS).
2.  **Pendekatan Iteratif:** Menggunakan manajemen *Stack* manual.

Aplikasi ini membangkitkan data dummy (ribuan folder dan file acak), lalu mengukur waktu eksekusi kedua algoritma tersebut secara *real-time*. Hasilnya disajikan dalam bentuk grafik garis interaktif dan tabel data presisi tinggi.

---

## 🎯 Untuk Siapa Project Ini Dibuat?

Project ini sangat cocok dan ditujukan untuk:

1.  **Mahasiswa Teknik Informatika / Ilmu Komputer**
    * Sebagai referensi atau bahan pembelajaran untuk mata kuliah **Struktur Data & Algoritma**.
    * Memahami konsep *Big O Notation* dan perbedaan efisiensi antara penggunaan *System Stack* (Rekursif) vs *Heap/Manual Stack* (Iteratif).
    * Contoh nyata implementasi struktur data *N-ary Tree*.

2.  **Dosen & Pengajar Pemrograman**
    * Sebagai alat bantu visual (*teaching aid*) di kelas untuk mendemonstrasikan bagaimana algoritma bekerja pada dataset yang besar.
    * Membuktikan secara empiris bahwa kompleksitas waktu kedua algoritma adalah linear $O(N)$.

3.  **Python Developer Pemula - Menengah**
    * Contoh studi kasus pembuatan aplikasi GUI Desktop menggunakan **Tkinter**.
    * Mempelajari cara mengintegrasikan **Matplotlib** ke dalam GUI.
    * Belajar teknik **Multi-threading** agar aplikasi tidak *freeze* (macet) saat melakukan komputasi berat.

---

## 🚀 Fitur Utama

* ✅ **Simulasi Data Masif:** Mampu men-generate struktur folder acak hingga puluhan ribu *nodes*.
* ✅ **Dual Benchmarking:** Menjalankan dua algoritma sekaligus dalam satu kali klik.
* ✅ **Visualisasi Grafik:** Grafik garis perbandingan waktu (milidetik) yang mudah dipahami.
* ✅ **Tabel Data Detail:** *Popup* tabel (Treeview) yang dapat di-scroll untuk melihat angka presisi di setiap checkpoint.
* ✅ **Responsive GUI:** Menggunakan *Threading* terpisah sehingga antarmuka tetap responsif selama proses berjalan.
* ✅ **Portable:** Tersedia dalam format `.exe` (Windows) yang dapat berjalan tanpa instalasi Python.

---

## 🛠️ Teknologi yang Digunakan

* **Bahasa:** [Python 3](https://www.python.org/)
* **GUI Framework:** Tkinter & Ttk (Bawaan Python)
* **Visualisasi Data:** [Matplotlib](https://matplotlib.org/)
* **Konkurensi:** Python `threading` module
* **Deployment:** [PyInstaller](https://pyinstaller.org/) (untuk build `.exe`)

---

## 💻 Cara Menjalankan

### Opsi 1: Menggunakan Aplikasi Portable (.exe)
1.  Download file `Folder Size Analyzer.exe` dari halaman Releases.
2.  Klik ganda aplikasi tersebut.
3.  Masukkan jumlah data (N) yang diinginkan, lalu klik **Mulai Analisis**.

### Opsi 2: Menjalankan dari Source Code
Pastikan Anda sudah menginstall Python.

1.  **Clone repository ini:**
    ```bash
    git clone [https://github.com/LionNite/folder-size-analyzer.git](https://github.com/LionNite/folder-size-analyzer.git)
    ```
2.  **Install library yang dibutuhkan:**
    ```bash
    pip install matplotlib
    ```
    *(Tkinter biasanya sudah terinstall otomatis bersama Python)*
3.  **Jalankan aplikasi:**
    ```bash
    python main.py
    ```

---

## 📂 Struktur Folder

```text
Folder-Size-Analyzer/
│
├── main.py        # Entry point aplikasi & Kode GUI (View)
├── logic.py       # Struktur data & Algoritma inti (Model/Controller)
└── Logo_App.ico       # Ikon aplikasi
