nilai_uts = float(input("Nilai UTS: ")) 
nilai_uas = float(input("Nilai UAS: ")) 
nilai_tugas = float(input("Nilai Tugas: ")) 
Hnilai_uts = nilai_uts * 0.3
Hnilai_uas = nilai_uas * 0.3
Hnilai_tugas = nilai_tugas * 0.4
total_nilai = Hnilai_uts + Hnilai_uas + Hnilai_tugas

if total_nilai >= 85: 
    print("Nilai Akhir = A")
    print("Selamat, Anda lulus dengan nilai A!")
elif total_nilai >= 70: 
    print("Nilai Akhir = B")
    print("Bagus, Anda lulus dengan nilai B!")
elif total_nilai >= 60: 
    print("Nilai Akhir = C")
    print("Anda lulus dengan nilai C, perbaiki di ujian berikutnya.")
else: 
    print("Nilai Akhir = D")
    print("Maaf, Anda tidak lulus. Silakan coba lagi di semester berikutnya.")
exit()

#------------------------- 4. Login Sederhana -------------------------
user = input("username = ") 
passw = input("password = ") 
username = "admin" 
password = "123" 

if user == username and passw == password: 
    print("Login Berhasil!") 
else: 
    print("Login gagal. Coba Lagi!")
exit()

#------------------------- 3. Menghitung Nilai Akhir Mahasiswa ------------------------- 
nilai_uts = float(input("Nilai UTS: ")) 
nilai_uas = float(input("Nilai UAS: ")) 
nilai_tugas = float(input("Nilai Tugas: ")) 
Hnilai_uts = nilai_uts * 0.3
Hnilai_uas = nilai_uas * 0.3
Hnilai_tugas = nilai_tugas * 0.4
total_nilai = Hnilai_uts + Hnilai_uas + Hnilai_tugas

if total_nilai >= 85: 
    print("Nilai Akhir = A")
elif total_nilai >= 70: 
    print("Nilai Akhir = B")
elif total_nilai >= 60: 
    print("Nilai Akhir = C")
else: 
    print("Nilai Akhir = D")
exit()
#------------------------- 2. Cek Bilangan Ganjil atau Genap -------------------------
bilangan = int(input("Masukan bilangan: "))
if bilangan % 2 == 0: 
    print("Bilangan genap")
elif bilangan % 2 != 0:
    print("Bilangan ganjil")
exit()

#------------------------- 1. Cek Angka Positif atau Negatif -------------------------
angka = int(input("Masukkan angka: "))

if angka > 0:
    print("Angka positif")
elif angka < 0:
    print("Angka negatif")
elif angka == 0:
    print("Angka nol")