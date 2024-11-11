import tkinter as tk
from tkinter import messagebox

def hasil_prediksi():
    try:
        for entry in entries:
            nilai = int(entry.get())
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
        hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
    except ValueError:
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")
root.resizable(False, False)
root.configure(bg="yellow")  # Mengubah Background menjadi kuning

judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"), fg="Purple", bg="Black")
judul_label.grid(row=0, column=0, columnspan=2, pady=20)

labels = []
entries = []

# Buat label dan kolom entri untuk 10 mata pelajaran
for i in range(10):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:", bg="yellow")
    label.grid(row=i+1, column=0, padx=20, pady=5, sticky='w')
    entry = tk.Entry(root)
    entry.grid(row=i+1, column=1, padx=20, pady=5)
    labels.append(label)
    entries.append(entry)

# Tombol untuk memicu prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.grid(row=11, column=0, columnspan=2, pady=20)

# Label untuk menampilkan hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 12), bg="yellow")
hasil_label.grid(row=12, column=0, columnspan=2, pady=10)

root.mainloop()
