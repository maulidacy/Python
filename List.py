#------------------------Membalik Kata dalam List------------------------
kata = ["apel", "pisang", "mangga"]
kata_terbalik = kata[::-1]
print(kata_terbalik) 

exit()


#------------------------Mencari Kata Terpanjang dalam List#------------------------
kata = ["aku", "kamu", "dia", "kita", "mereka"]
kata_terpanjang = max(kata, key=len)
print(kata_terpanjang) # Output: mereka
exit()


#------------------------Menyusun List dari Input Pengguna------------------------
name_new = []
i = 0

while True:
    name = input(f"Masukkan nama ke-{i + 1}: ")
    if name == 0:
        break
    name_new.append(name)
    print("List nama: ", name_new)
exit()

#------------------------Menyusun List dari Input Pengguna------------------------
name_new = []
i = 0

while True:
    name = input(f"Masukkan nama ke-{i + 1}: ")
    if name == "0":  # Check for string input "0" to break the loop
        break
    name_new.append(name)
    print("List nama: ", name_new)
    i += 1  # Increment the counter
exit()

#------------------------Menghapus Duplikat dalam List------------------------
angka = [1, 2, 2, 3, 4, 4, 5, 5, 6]

angka_baru = list(set(angka)) # Menghapus duplikat dengan mengubah list menjadi set
print(angka_baru)
exit()


#------------------------Mencari Nilai Maksimum dan Minimum dalam List------------------------
angka = [4, 7, 1, 9, 12, 5]
max_angka = max(angka)
min_angka = min(angka)

print("Nilai maksimum: ", max_angka)
print("Minimum Nilai: ", min_angka)
exit()


#------------------------Menggabungkan dan Mengurutkan Dua List------------------------
list1 = [5, 10, 15]  
list2 = [2, 8, 12]

print("List sebelum digabungkan:")
print("List 1: ", list1)
print("List 2: ", list2)

# Menggabungkan dua list menggunakan fungsi extend() dan sort() untuk mengurutkan list gabungan
list_gabungan = list1.copy()  # Membuat salinan list1
list_gabungan.extend(list2)  # Menggabungkan list2 ke list1

# Mengurutkan list gabungan
list_gabungan.sort()
print("List Gabungan yang Telah Diurutkan: ", list_gabungan)
exit()


#------------------------Menentukan Angka Ganjil dan Genap dalam List------------------------
angka = [10, 15, 20, 25, 30, 35, 40]
ganjil = [x for x in angka if x % 2 != 0]
genap = [x for x in angka if x % 2 == 0]

print("List angka genap: ", genap)
print("List angka ganjil: ", ganjil)
exit()


#------------------------Menghitung Jumlah Kemunculan Elemen dalam List------------------------
angka = [3, 5, 7, 3, 3, 5, 9, 7, 3, 3]
jumlah = angka.count(3)

print(f"Angka 3 muncul sebanyak: {jumlah} kali")
exit()


#------------------------Menyalin dan Membandingkan List------------------------
kota = ['Jakarta', 'Surabaya', 'Bandung', 'Medan', 'Bali'] 
kota_baru = kota.copy()
kota_baru.append("Yogyakarta")

print("Kota Awal: ", kota)
print("Kota Update: ", kota_baru)

# Membandingkan kedua list
if kota == kota_baru:
    print("List sama.")
else:
    print("List tidak sama.")

exit()



#------------------------Menghitung Total dan Rata-rata List------------------------
angka = [10, 20, 30, 40, 50]
jumlah_angka = len(angka)
total = sum(angka)
rata_rata = total / jumlah_angka

print("Total: ", total)
print("Rata-rata: ", rata_rata)
exit()


#------------------------Menghitung Jumlah Elemen dalam List------------------------
bilangan = [2, 4, 6, 8, 10, 12, 14]
jumlah_bilangan = len(bilangan)

print("Jumlah elemen dalam list: ", jumlah_bilangan)
exit()


#------------------------List 2 Dimensi (Nested List)------------------------
siswa = [
    [10, 12, 14],  # Minggu 1
    [11, 13, 15],  # Minggu 2
    [9, 10, 12]    # Minggu 3
]

print(siswa[1][2]) #Cetak jumlah siswa di minggu ke-2, hari ke-3.
print(siswa[0][0]) #Cetak jumlah siswa di minggu pertama, hari pertama.
exit()



#------------------------Mengurutkan dan Membalik List------------------------
angka = [5, 2, 9, 1, 7]
print("List awal: ", angka)

# Mengurutkan list dalam urutan ascending
angka.sort()
print("List setelah diurutkan: ", angka)
# Membalik list
angka.reverse()
print("List setelah dibalik: ", angka)
exit()


#------------------------Mencari Elemen dalam List------------------------
hewan = ["kucing", "anjing", "kelinci", "sapi"]

for cek in hewan:
    cek = input("cek hewan: ")
    if cek in hewan:
        print(f"{cek} ditemukan")
        break
    else:
        print(f"{cek} tidak ditemukan")
exit()


#------------------------Perulangan dalam List------------------------
name = ["Andi", "Budi", "Cici", "Dodi"]

for i in name:
    print(i)
exit()


#------------------------Menambahkan dan Menghapus Elemen------------------------
angka = []
angka.append(10) #menambahkan
angka.append(20)
angka.append(30)
angka.append(40)
angka.append(50)
angka.remove(30) #menghapus

print(angka)
exit()


#------------------------Mengubah Elemen dalam List------------------------
warna = ["merah", "biru", "hijau", "kuning"]
warna[2] = "ungu"
warna[0] = "hitam"

print(warna)
exit()


#------------------------Buat dan Akses List------------------------
buah = ["apel", "durian", "pisang", "semangka", "jeruk"]
print(buah[0], buah[-3], buah[-1])

print(buah[0])
print(buah[-3])
print(buah[-1])
