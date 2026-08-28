# Belajar perulangan (loop) di python

# Mengulang sebanyak N kali
print("---Cetak angka 1 sampai 5---")
for i in range(1,6):
    print(f"perulangan ke{i}")

# Mengiterasin (menjelajah) isi list
print("\n--- Daftar matkul semester ini ---")
matkul_list = ["Algoritma pemrograman","Struktur data","Jaringan komputer","Basis data"]
for matkul in matkul_list:
    print(f"- mata kuliah:{matkul}")