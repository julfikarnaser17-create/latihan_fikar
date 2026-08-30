# Belajar fungsi (def) di Python
#  1. Membuat fungsi untuk menyapa
def sapa_user(nama):
    print(f"Halo {nama}! selamat datang di latihan python.")

# 2. Membuat fungsi dengan pengembalian nilai (return)
def hitung_nilai_akhir (tugas, uts): 
    total = (tugas * 0.4) + (uts * 0.6)
    return total

# Memangil fungsi yang sudah dibuat
sapa_user("fikar")
nilai_final = hitung_nilai_akhir(80, 90)
print(f"Nilai Akhir Praktikum : {nilai_final}")
