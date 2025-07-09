#------------------------- 1. Buat 3 variabel: nama (string), umur (integer), tinggi (float) -------------------------
nama = "Budi"
umur = 0
tinggi = 1.75
#------------------------- 2. Cetak kalimat: "Halo, nama saya ___, umur saya ___ tahun." -------------------------
print(f"Nama: {nama}, Umur: {umur} tahun, Tinggi: {tinggi} meter")

#------------------------- 3. Hitung dan tampilkan hasil dari: 5 + 2 * 10 - 3 / 2 -------------------------
a = 5
b = 2
c = 10
d = 3
Hitung = a+b*c-d/b
print(f"Hasil perhitungan: {Hitung}")

#------------------------- 4. Ubah dan Tampilkan Tipe Data -------------------------
nilaiA = "10"
nilaiB = 5
nilaiC = 2.4

print(f"NilaiA awal: {nilaiA}, Tipe data: {type(nilaiA)}, -> setelah diubah: {int(nilaiA)}, Tipe data: {type(int(nilaiA))}")
print(f"NilaiB awal: {nilaiB}, Tipe data: {type(nilaiB)}, -> setelah diubah: {float(nilaiB)}, Tipe data: {type(str(nilaiB))}")
print(f"NilaiC awal: {nilaiC}, Tipe data: {type(nilaiC)}, -> setelah diubah: {int(nilaiC)}, Tipe data: {type(int(nilaiC))}")
