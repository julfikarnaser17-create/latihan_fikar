# Belajar percabangan (if-elif-else) di python
nilai = int(input("masukan nilai: "))
if nilai >= 85:
    print("Grade: A (sangat memuaskan)")
elif nilai >= 70:
    print("Grade B (bagus)")
elif nilai >= 60:
    print("Grade C (cukup)")
else:
    print("Grade D (perlu perbaikan)")