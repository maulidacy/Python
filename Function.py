# Gunakan return jika ingin menggunakan kembali hasil dari fungsi itu (misalnya disimpan, dicetak, dibandingkan, dsb).
# Gunakan print() jika hanya ingin menampilkan sesuatu, tapi tidak perlu hasilnya.

#---------------------------------Kasir Sederhana------------------------------------

def sapa_pembeli(nama="Pembeli"):
    print(f"Halo {nama}, selamat datang di Warung Python!")

sapa_pembeli(input("Halo, siapa nama Anda? "))


def tampilkan_menu():
    print("\n======Daftar Menu=======")
    print("1. Nasi Goreng - Rp. 15000")
    print("2. Mie Ayam - Rp. 5000")
    print("3. Sambala sambalado - Rp. 3000")
    print("4. Telor ceplok - Rp. 3000")
    print("5. Teh pait - Rp. 3000")
    print("========================")


# Daftar menu
menu_makanan = ["Nasi Goreng", "Mie Ayam", "Sambala Sambalado", "Telor Ceplok", "Teh pait"]
harga_makanan = [15000, 12000, 4000, 3000, 3000]

# List untuk menyimpan harga pesanan
pesanan_harga = []

def jumlah():
    jumlah_dibeli = int(input("Jumlah = "))
    return jumlah_dibeli

while True:
    tampilkan_menu()
    try:
        pilihan = int(input("Pilih menu (tekan 0 untuk keluar): "))
    except ValueError:
        print("Masukkan angka antara 1 sampai 5!")
        continue

    if pilihan == 1:
        print(f"{menu_makanan[0]} - Rp. 4000")
        jumlah()
    elif pilihan == 2:
        print(f"{menu_makanan[1]} - Rp. 5000")
        jumlah()
    elif pilihan == 3:
        print(f"{menu_makanan[2]} - Rp. 3000")
        jumlah()
    elif pilihan == 4:
        print(f"{menu_makanan[3]} - Rp. 3000")
        jumlah()
    elif pilihan == 5:
        print(f"{menu_makanan[4]} - Rp. 3000")
        jumlah()
    elif pilihan == 0:
        break
    else:
        print("Pilihan tidak valid!")


keranjang = []
keranjang.append(menu_makanan[pilihan]) #setiap kali user pilih barang
print(keranjang)


        


exit()




#--------------------------------- Fungsi Mengolah List--------------------------------------
def hitung_rata(nilai_list):
    return sum (nilai_list) / len (nilai_list) # hitung rata-rata

print("Hasil: ", hitung_rata([80, 90, 75]))
exit()

#---------------------------------Panggil fungsi ini tanpa parameter dan dengan parameter.------------------------------
def greet(nama="User"):
    print(f"Halo, {nama}")

# Panggilan tanpa parameter → pakai default "User"
greet()

# Panggilan dengan parameter → override default
greet("maul")
exit()

#---------------------------------Fungsi Menghitung Luas Persegi--------------------------------------------
def hitung_persegi(sisi):
    return sisi*sisi

print(hitung_persegi(5))
exit()

#---------------------------------Fungsi dengan Parameter Biasa--------------------------------------------
def sapa_user(nama):
    print(f"Halo {nama}, selamat datang!")

sapa_user("maul")
exit()

#---------------------------------Fungsi tanpa Parameter--------------------------------------------
def tampilkan_salam():
    print("Halo, selamat datang di Python")

tampilkan_salam()
exit()

#--------------------------------Fungsi tanpa Parameter-------------------------------
def tampilkan_menu():
    print("======Daftar Menu=======")
    print("1. Nasi")
    print("2. Ayam")
    print("3. Sambala sambalado")
    print("4. Telor Ceplok")
    print("========================")

tampilkan_menu()
exit()

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