# Belajar mengabungkan list [], fungsi (), & perulangan for
# 1. Membuat list [], berisi daftar server (Contoh kasus DevOps)
daftar_server = ["Server-Web","Server-DataBase","Server-Backup"]
print("--- mengecek status server ---")
# 2. Mengunakan perulangan for dan fungsi print()
for server in daftar_server:
    print(f"Status: {server} sedang berjalan (ONLINE)")