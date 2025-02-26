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
