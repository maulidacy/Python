
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