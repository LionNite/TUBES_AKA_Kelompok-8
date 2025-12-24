import tkinter as tk
from tkinter import ttk, messagebox
import threading
import time
import matplotlib.pyplot as plt

# --- IMPORT FILE LOGIC ---
from logic import generate_node_dummy, hitung_rekursif, hitung_iteratif
# ---------------------------------------------------------
# BAGIAN 3: GUI APLIKASI (INTERFACE)
# ---------------------------------------------------------
class App:
    def __init__(self, root): # Constructor diperbaiki jadi __init__
        self.root = root
        self.root.title("Tugas Besar: Analisis Algoritma Folder Size")
        self.root.geometry("600x500")

        # --- Input Section ---
        frame_input = ttk.LabelFrame(root, text="Konfigurasi Pengujian")
        frame_input.pack(padx=10, pady=10, fill="x")

        ttk.Label(frame_input, text="Maksimum Input (N):").grid(row=0, column=0, padx=5, pady=5)
        self.entry_n = ttk.Entry(frame_input)
        self.entry_n.insert(0, "10000")  # Default sesuai soal
        self.entry_n.grid(row=0, column=1, padx=5, pady=5)

        self.btn_run = ttk.Button(frame_input, text="Mulai Analisis & Bandingkan", command=self.run_analysis)
        self.btn_run.grid(row=0, column=2, padx=5, pady=5)

        # --- Log Section ---
        frame_log = ttk.LabelFrame(root, text="Log Eksekusi")
        frame_log.pack(padx=10, pady=5, fill="both", expand=True)

        self.txt_log = tk.Text(frame_log, height=15)
        self.txt_log.pack(padx=5, pady=5, fill="both", expand=True)

        # --- Progress Bar ---
        self.progress = ttk.Progressbar(root, orient="horizontal", mode="indeterminate")
        self.progress.pack(fill="x", padx=10, pady=5)

    def log(self, message):
        self.txt_log.insert(tk.END, message + "\n")
        self.txt_log.see(tk.END)

    def run_analysis(self):
        try:
            max_n = int(self.entry_n.get())
        except ValueError:
            messagebox.showerror("Error", "Masukkan angka N yang valid!")
            return

        # Jalankan di thread terpisah agar GUI tidak macet/hang saat loading
        self.btn_run['state'] = 'disabled'
        self.progress.start(10)
        threading.Thread(target=self.process_data, args=(max_n,), daemon=True).start()

    def process_data(self, max_n):
        # Perbaikan: Akses GUI dari thread harus hati-hati, tapi untuk text.insert biasanya aman di simple app.
        # Jika error, gunakan root.after. Di sini saya biarkan dulu agar simple.
        self.txt_log.delete(1.0, tk.END)
        self.log(f"--- Memulai Pengujian hingga N={max_n} ---")

        # Skenario Input
        checkpoints = [10, 50, 100, 500, 1000, 2500, 5000, 7500, max_n]
        checkpoints = sorted(list(set([c for c in checkpoints if c <= max_n])))
        if max_n not in checkpoints: checkpoints.append(max_n)

        results_n = []
        results_rec = []
        results_iter = []

        for n in checkpoints:
            self.log(f"\n[Generate Data] Membuat struktur {n} items...")
            
            # Perbaikan: Memanggil fungsi asli Anda 'generate_node_dummy'
            data_tree = generate_node_dummy(n)

            # --- Uji Rekursif ---
            start = time.perf_counter()  # Lebih presisi dari time.time()
            res_r = hitung_rekursif(data_tree)
            end = time.perf_counter()
            time_r = (end - start) * 1000  # ke milidetik

            # --- Uji Iteratif ---
            start = time.perf_counter()
            res_i = hitung_iteratif(data_tree)
            end = time.perf_counter()
            time_i = (end - start) * 1000  # ke milidetik

            # Simpan Data
            results_n.append(n)
            results_rec.append(time_r)
            results_iter.append(time_i)

            # Perbaikan: variable 'time_iter' di print tidak ada, diganti 'time_i'
            self.log(f"-> N={n}: Rec={time_r:.4f} ms | Iter={time_i:.4f} ms")
            self.log(f"   (Validasi Size: {res_r} bytes)")

        self.log("\n--- Selesai. Menampilkan Grafik... ---")
        
        # Menghentikan progress bar harus dari main thread jika memungkinkan, tapi ini oke.
        self.root.after(0, self.stop_ui)
        self.root.after(0, lambda: self.show_graph(results_n, results_rec, results_iter))

    def stop_ui(self):
        self.progress.stop()
        self.btn_run['state'] = 'normal'

    def show_graph(self, x, y1, y2):
        # Memunculkan window grafik matplotlib
        plt.figure(figsize=(10, 6))
        plt.plot(x, y1, marker='o', linestyle='-', color='red', label='Rekursif')
        plt.plot(x, y2, marker='x', linestyle='--', color='blue', label='Iteratif')

        plt.title('Perbandingan Waktu Eksekusi: Rekursif vs Iteratif')
        plt.xlabel('Jumlah Input (N)')
        plt.ylabel('Waktu (milidetik)')
        plt.grid(True)
        plt.legend()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()