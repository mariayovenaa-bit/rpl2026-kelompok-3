# Program Kuis Interaktif

print("Selamat datang di Kuis Python!")

nama = input("Masukkan nama kamu: ")
print("Halo,", nama)

jawaban = input("Ibu kota Indonesia adalah? ")
if jawaban.lower() == "jakarta":
    print("Benar! Kamu hebat.")
else:
    print("Belum tepat. Jawaban yang benar adalah Jakarta.")