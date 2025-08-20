# Gunakan return jika ingin menggunakan kembali hasil dari fungsi itu (misalnya disimpan, dicetak, dibandingkan, dsb).
# Gunakan print() jika hanya ingin menampilkan sesuatu, tapi tidak perlu hasilnya.
# print() hanya menampilkan sesuatu di layar, sementara return benar-benar memberikan nilai dari fungsi tersebut untuk digunakan di bagian lain dari program
# def sapa(nama): # nama = parameter (tempat masuknya data ke fungsi) atau kotak kosong di fungsi
# sapa("Budi")  # Budi = argumen (nilai yang dikirim saat fungsi dipanggil)

#----------------------------
teks = []

def clean_text(text):
    return clean_text.lower()  # Mengubah teks menjadi huruf kecil

text = input("Masukkan teks: ")


#=--------------------------- Key=len pada max() ---------------------------
# Program untuk menunjukkan penggunaan
kalimat = "saya suka belajar python"
kata_list = kalimat.split()

"""Kalau tidak pakai key=len, maka fungsi max() akan mencari kata “terbesar” 
berdasarkan urutan alfabet (lexicographical order), bukan berdasarkan panjangnya"""

print("Tanpa key=len:", max(kata_list))  
print("Dengan key=len:", max(kata_list, key=len))
exit()

#--------------------------- Hitung Jumlah Kata, menampikan kata terpanjang ---------------------------
# Program untuk menghitung jumlah kata dalam kalimat yang dimasukkan oleh pengguna
def hitung_jumlah_kata(kata):
    """Fungsi untuk menghitung jumlah kata dalam kalimat"""
    if not kata:  # Cek jika kata kosong
        return 0
    return len(kata.split())  # Menghitung jumlah kata dengan memisahkan berdasarkan spasi

def kata_terpanjang(kata):
    """Fungsi untuk menemukan kata terpanjang dalam kalimat"""
    if not kata:  # Cek jika kata kosong
        return ""
    kata_list = kata.split()  # Memisahkan kalimat menjadi daftar kata
    return max(kata_list, key=len)  # Mengembalikan kata terpanjang

kalimat = input("Masukkan kalimat: ")

print(f"Jumlah kata dalam kalimat: {hitung_jumlah_kata(kalimat)}")
print(f"Kata terpanjang dalam kalimat: {kata_terpanjang(kalimat)}")
exit()

#--------------------------- Hitung Rata-Rata ---------------------------
# Program untuk menghitung rata-rata dari daftar nilai yang dimasukkan oleh pengguna
kumpulan_nilai = []

def hitung_rata_rata(kumpulan_nilai):
    """Fungsi untuk menghitung rata-rata dari daftar nilai"""
    if not kumpulan_nilai:  # Cek jika daftar kosong
        return 0
    return sum(kumpulan_nilai) / len(kumpulan_nilai)

while True:
    nilai_input = input("Masukkan nilai (ketik Y/y untuk keluar): ")

     # cek dulu kalau user mau keluar
    if nilai_input.lower() == 'y':
        print(f"Rata-rata nilai: {hitung_rata_rata(kumpulan_nilai)}")
        break

    try:
        nilai = float(nilai_input)  # ubah jadi angka
        kumpulan_nilai.append(nilai)  # Menambahkan nilai ke daftar
    except ValueError:
        print("Input tidak valid! Harap masukkan angka.")
        exit()
exit()

#--------------------------- Konversi Suhu ---------------------------
def konversi_fahrenheit(suhu):
    """Fungsi untuk mengonversi suhu dari Celcius ke Fahrenheit"""
    fahrenheit = (suhu * 9/5) + 32 
    return fahrenheit
def konversi_kelvin(suhu):
    """Fungsi untuk mengonversi suhu dari Celcius ke Kelvin"""
    kelvin = suhu + 273.15
    return kelvin

try:
    suhu = float(input("Masukkan suhu dalam Celcius: "))
    # fahrenheit = konversi_fahrenheit(suhu) # gini juga bisa, tapi lebih rapi kalau langsung di print
    # kelvin = konversi_kelvin(suhu)
    print(f"Dalam Fahrenheit: {konversi_fahrenheit(suhu)}") # lebih rapi
    print(f"Dalam Kelvin: {konversi_kelvin(suhu)}")
except ValueError:
    print("Input tidak valid! Harap masukkan angka.")
    exit()
exit()

#------------------------- Cek Ganjil Genap -------------------------
def ganjil_genap(angka):
    """Fungsi untuk mengecek apakah angka ganjil atau genap"""
    if angka % 2 == 0:
        print("Genap")
    else:
        print("Ganjil")

try:
    angka = int(input("Masukkan angka: "))
    ganjil_genap(angka)
except ValueError:
    print("Input harus berupa angka")

exit()

#------------------------- Hitung Jumlah Huruf Vokal -------------------------
huruf_vokal = "aiueo"
jumlah_huruf = 0

def hitung_huruf_vokal(kalimat):
    global jumlah_huruf  # Menggunakan variabel global untuk menyimpan jumlah huruf vokal
    for huruf in kalimat.lower():  # Menggunakan lower() untuk mengabaikan huruf kapital
        if huruf in huruf_vokal:
            jumlah_huruf += 1
    return jumlah_huruf

try:
    kalimat = input("Masukkan kalimat: ")
except EOFError:
    print("Tidak ada input yang diberikan.")
    exit()
print(f"Jumlah huruf vokal dalam kalimat: {hitung_huruf_vokal(kalimat)}")
exit()

#--------------------------------- Cek Ganjil Genap --------------------------------------------
# Fungsi untuk mengecek apakah angka genap atau ganjil
def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "Angka genap"
    else:
        return "Angka ganjil"
    
try:
    angka = int(input("Masukkan angka: "))
    print(cek_ganjil_genap(angka))
except ValueError:
    print("Input tidak valid! Harap masukkan angka.")
    exit()

#-------------------------------------------------------------------------------------------------
angka = [1, 2, 3, 4, 5]

def hitung_rata_rata(angka):
    hasil = sum(angka)/len(angka)
    return hasil

print("Rata-rata:", hitung_rata_rata(angka))
exit()

#---------------------------------Kasir Sederhana (Revisi Bro)------------------------------------
'''Kerangka Program Kasir Sederhana
1. Definisikan daftar menu dan harga
   Buat list atau dictionary untuk menyimpan nama makanan/minuman beserta harganya.
2. Fungsi tampilkan_menu()
   Tanpa parameter.
   Menampilkan daftar menu beserta harga.
3. Fungsi hitung_total(daftar_harga)
   Parameter: list harga yang dibeli.
   Menghitung total seluruh harga dalam list.
   Mengembalikan nilai total.
4. Fungsi beri_diskon(total, diskon=0.1)
   Parameter: total (wajib) dan diskon (default 0.1 atau 10%).
   Menghitung harga setelah diskon. 
   Mengembalikan harga yang sudah dipotong.
5. Fungsi sapa_pembeli(nama="Pembeli")
   Parameter default nama.
   Menampilkan ucapan sambutan.
6. Bagian utama program
   Panggil sapa_pembeli() (bisa pakai default atau input nama).
   Panggil tampilkan_menu().
   Minta pembeli memilih barang (gunakan loop).
   Simpan harga barang yang dipilih ke list.
   Hitung total dengan hitung_total().
   Tawarkan diskon, hitung dengan beri_diskon().
   Tampilkan total akhir ke pembeli.'''

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