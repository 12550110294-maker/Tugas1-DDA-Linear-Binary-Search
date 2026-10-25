from book import Buku
import pandas as pd
import time

# 1. FUNGSI LINEAR SEARCH
def linear_search(koleksi_buku, target_judul):
    jumlah_komparasi = 0
    target = target_judul.lower()
    
    for buku in koleksi_buku:
        jumlah_komparasi += 1
        if buku.title.lower() == target: 
            return buku, jumlah_komparasi
            
    return None, jumlah_komparasi

# 2. FUNGSI BINARY SEARCH
def binary_search(koleksi_buku, target_judul):
    jumlah_komparasi = 0
    kiri = 0
    kanan = len(koleksi_buku) - 1
    target = target_judul.lower()

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        judul_tengah = koleksi_buku[tengah].title.lower()
        jumlah_komparasi += 1
        
        if judul_tengah == target:
            return koleksi_buku[tengah], jumlah_komparasi
        elif judul_tengah < target:
            kiri = tengah + 1
        else:
            kanan = tengah - 1
            
    return None, jumlah_komparasi

# 3. FUNGSI UJI ALGORITMA & TAMPILKAN HASIL
def uji_algoritma(dataset_asli, n, target_judul, skenario):
    data_uji = dataset_asli[:n]
    print(f"\n--- Skenario: {skenario} | Input (n): {n} ---")
    print(f"Mencari judul: '{target_judul}'")
    
    # Eksekusi Linear Search
    start_time = time.perf_counter()
    hasil_ls, komparasi_ls = linear_search(data_uji, target_judul)
    waktu_ls = time.perf_counter() - start_time
    
    # Eksekusi Binary Search (Data wajib diurutkan terlebih dahulu)
    data_uji_sorted = sorted(data_uji, key=lambda x: x.title.lower())
    start_time = time.perf_counter()
    hasil_bs, komparasi_bs = binary_search(data_uji_sorted, target_judul)
    waktu_bs = time.perf_counter() - start_time
    
    # MENAMPILKAN INFORMASI BUKU
    if hasil_ls is not None:
        print(f"Status: DATA DITEMUKAN!")
        print(f"Detail Buku: {hasil_ls.title} | Penulis: {hasil_ls.author} | Kategori: {hasil_ls.category}")
    else:
        print(f"Status: DATA TIDAK DITEMUKAN!")
        
    print(f"Linear Search -> Komparasi: {komparasi_ls}, Waktu: {waktu_ls:.6f} detik")
    print(f"Binary Search -> Komparasi: {komparasi_bs}, Waktu: {waktu_bs:.6f} detik")

# 4. EKSEKUSI UTAMA
if __name__ == "__main__":
    print("Membaca dataset, mohon tunggu...")
    # Menggunakan nama "buku.csv" sesuai dengan nama file di VS Code Anda
    df = pd.read_csv("buku.csv") 
    
 # Memasukkan data dari CSV ke dalam List of Objects (kelas Buku)
    dataset_buku = []
    for index, row in df.iterrows():
        # Menangani jika ada data kosong agar program tidak crash
        title = str(row['title']) if pd.notna(row['title']) else ""
        author = str(row['authors']) if pd.notna(row['authors']) else ""
        category = str(row['categories']) if 'categories' in df.columns and pd.notna(row['categories']) else "-"
        
        # Kirim angka 0 untuk harga karena dataset tidak punya kolom price
        buku = Buku(title, author, category, 0)
        dataset_buku.append(buku)
    print(f"Total data dimuat: {len(dataset_buku)} buku\n")

    # Fungsi pembantu untuk menjalankan ke-4 skenario secara otomatis
    def jalankan_skenario(n_input):
        data_uji = dataset_buku[:n_input]
        data_uji_sorted = sorted(data_uji, key=lambda x: x.title.lower())
        
        target_awal = data_uji_sorted[0].title
        target_tengah = data_uji_sorted[n_input // 2].title
        target_akhir = data_uji_sorted[-1].title
        target_tidak_ada = "Buku Ini Pasti Tidak Ada 123"

        print(f"\n================ PENGUJIAN UNTUK n = {n_input} ================")
        uji_algoritma(dataset_buku, n_input, target_awal, "Data di posisi awal")
        uji_algoritma(dataset_buku, n_input, target_tengah, "Data di posisi tengah")
        uji_algoritma(dataset_buku, n_input, target_akhir, "Data di posisi akhir")
        uji_algoritma(dataset_buku, n_input, target_tidak_ada, "Data tidak ditemukan")

    # Menjalankan untuk n = 100, 1000, dan 10000
    jalankan_skenario(100)
    jalankan_skenario(1000)
    jalankan_skenario(10000)

