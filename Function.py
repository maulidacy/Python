# Gunakan return jika ingin menggunakan kembali hasil dari fungsi itu (misalnya disimpan, dicetak, dibandingkan, dsb).
# Gunakan print() jika hanya ingin menampilkan sesuatu, tapi tidak perlu hasilnya.

#------------------------Hitung Rata-Rata-------------------------------------
def hitung_rata(nilai):
    return sum(nilai) / len(nilai)

print("Hasil: ", hitung_rata([1, 2, 3, 4, 5]))
exit()

#------------------------Menghitung Total Harga Barang------------------------
# Input dari pengguna
nama_barang = input("Masukkan nama barang: ")
harga_barang = float(input("Masukkan harga barang (dalam angka): "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

# Fungsi untuk menghitung total harga
def hitung_total(harga, jumlah):
    return harga * jumlah

# Pemanggilan fungsi
total_harga = hitung_total(harga_barang, jumlah_barang) # Variabel total_harga digunakan untuk menyimpan hasil dari fungsi

# Output hasil
print("\n============ Daftar belanja ============")
print("Barang:", nama_barang)
print("Total harga:", total_harga)
print("============= Terima kasih =============")
exit()

#--------------------------------------------------------------
angka = input("Masukkan angka: ")
def cek_genap(angka):
    if angka % 2 == 0:
        return True
    else:
        return False
hasil = cek_genap(int(angka))
print(hasil) 
exit()

#--------------------------------------------------------------
def hitung_total(harga, jumlah, diskon):
    return harga * jumlah - (harga * jumlah * diskon / 100)
total = hitung_total(50000, 3, 20)
print("Total akhir:", total)

#versi rapi
def hitung_total(harga, jumlah, diskon):
    total = harga * jumlah
    potongan = total * diskon / 100
    return total - potongan
total = hitung_total(50000, 3, 20)
print(f"Total harga setelah diskon: {total}")
#-------------------------------------------------------------
def nilai_tertinggi(a, b, c):
    nilai_tertinggi = [a, b, c]
    largest_number = max(nilai_tertinggi)
    return largest_number
print(nilai_tertinggi(10, 30, 20))

#versi if else
def nilai_tertinggi(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c
print(nilai_tertinggi(10, 30, 20))
exit()
#-------------------------------------------------------------
def jumlah(a, b): 
    return a + b 
hasil = jumlah (5, 4) 
print("Hasilnya:", hasil) 
exit()
#-------------------------------------------------------------
def luas_lingkaran(jari_jari): 
    return 3.14 * jari_jari * jari_jari 
hasil = luas_lingkaran(3) 
print("Hasilnya:", hasil)
exit()
#-------------------------------------------------------------
def cek_genap(n):
    return n % 2 == 0
hasil = cek_genap(5)
print(hasil) 
exit()
#-------------------------------------------------------------
def total_harga(harga, jumlah):
    total = harga * jumlah
    if total > 100000:
        total -= total * 0.10  # diskon 10%
    return total

total = total_harga(60000, 2)
print(f"Total harga setelah diskon: {total}")
exit()
#-------------------------------------------------------------
def cek_genap(n):
    return n % 2 == 0
hasil = cek_genap(6)
print(hasil)
#---------------------------------------------------------------
def jumlah(a, b):
    return a + b 
hasil = jumlah (5, 4) 
print("Hasilnya:", hasil)

def tambah(a, b):
    return a + b

hasil = tambah(3, 4)
print("Hasilnya:", hasil)

#------------------------- Function -------------------------
def ucapan(): print("Selamat belajar Python!")
ucapan() 

def luas_persegi(sisi): 
    hasil = sisi * sisi 
    print(f"Luas persegi adalah: {hasil}") 
luas_persegi(5) 
    
#------------------------- Parameter ganda -------------------------
def salam (nama, waktu): 
    print(f"Selamat {waktu}, {nama}!")
salam("Maulida", "pagi")