# Gunakan return jika ingin menggunakan kembali hasil dari fungsi itu (misalnya disimpan, dicetak, dibandingkan, dsb).
# Gunakan print() jika hanya ingin menampilkan sesuatu, tapi tidak perlu hasilnya.

def sapa_pembeli(nama="Pembeli"):
    """Menyapa pembeli dengan nama tertentu atau default."""
    print(f"Halo {nama}, selamat datang di Warung Python!")

def tampilkan_menu():
    """Menampilkan daftar menu makanan dan harga."""
    print("\n====== Daftar Menu =======")
    print("1. Nasi Goreng \t - Rp. 15000")
    print("2. Mie Ayam \t - Rp. 12000")
    print("3. Sambalado \t - Rp. 4000")
    print("4. Telor Ceplok\t - Rp. 3000")
    print("5. Teh Pait \t - Rp. 3000")
    print("==========================")

# --- Menggunakan kamus (dictionary) untuk menyimpan menu agar lebih rapi ---
daftar_menu = {
    1: {"nama": "Nasi Goreng", "harga": 15000},
    2: {"nama": "Mie Ayam", "harga": 12000},
    3: {"nama": "Sambalado", "harga": 4000},
    4: {"nama": "Telor Ceplok", "harga": 3000},
    5: {"nama": "Teh Pait", "harga": 3000}
}

def hitung_total(daftar_harga):
    """Menerima list harga dan menghitung totalnya."""
    total = sum(daftar_harga)
    return total

def beri_diskon(total, diskon=0.1):
    """Menghitung harga setelah diskon (default diskon = 10%)."""
    if total > 50000: # Contoh: diskon hanya berlaku jika total belanja > 50000
        diskon_amount = total * diskon
        total_setelah_diskon = total - diskon_amount
        return total_setelah_diskon
    else:
        return total

# --- PROGRAM UTAMA ---
if __name__ == "__main__":
    # Sapa pembeli
    nama_pembeli = input("Halo, siapa nama Anda? ")
    sapa_pembeli(nama_pembeli)

    pesanan_harga = []
    
    while True:
        tampilkan_menu()
        
        try:
            pilihan = int(input("Pilih menu (tekan 0 untuk selesai): "))
        except ValueError:
            print("Pilihan tidak valid, masukkan angka antara 0-5.")
            continue
            
        if pilihan == 0:
            break
        elif pilihan in daftar_menu:
            menu_terpilih = daftar_menu[pilihan]
            nama_menu = menu_terpilih["nama"]
            harga_menu = menu_terpilih["harga"]
            
            try:
                jumlah_dibeli = int(input(f"Berapa jumlah {nama_menu} yang ingin dibeli? "))
                if jumlah_dibeli <= 0:
                    print("Jumlah tidak valid. Masukkan angka positif.")
                    continue
                
                total_harga_item = harga_menu * jumlah_dibeli
                pesanan_harga.append(total_harga_item)
                print(f"✅ {nama_menu} sejumlah {jumlah_dibeli} ditambahkan ke keranjang!")
                
            except ValueError:
                print("Jumlah tidak valid, masukkan angka.")
                continue
        else:
            print("Pilihan tidak ada di menu. Silakan pilih lagi.")
            
    # --- PROSES PEMBAYARAN ---
    if not pesanan_harga:
        print("\nAnda tidak memesan apa pun. Sampai jumpa!")
    else:
        total_belanja = hitung_total(pesanan_harga)
        total_setelah_diskon = beri_diskon(total_belanja)
        
        print("\n========== Struk Belanja ===========")
        print(f"Total belanja sebelum diskon: Rp. {total_belanja:,}")
        
        if total_belanja > 50000:
            print(f"Selamat! Anda mendapatkan diskon 10%.")
            print(f"Total yang harus dibayar: Rp. {total_setelah_diskon:,}")
        else:
            print(f"Total yang harus dibayar: Rp. {total_belanja:,}")
        print("====================================")
            
        print("Terima kasih sudah berbelanja!")


exit()

#---------------------------------Kasir Sederhana (Revisi Bro)------------------------------------

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