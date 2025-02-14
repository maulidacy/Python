#------------------------Menghitung Pajak Berlapis (Progressive Tax)------------------------
def hitung_pajak(pendapatan):
    if pendapatan <= 5000000:
        return 0.05 * pendapatan
    elif pendapatan <= 10000000:
        return (5000000 * 0.05) + ((pendapatan - 5000000) * 0.10)
    else:
        return (5000000 * 0.05) + (5000000 * 0.10) + ((pendapatan - 10000000) * 0.15)

pendapatan1 = 12000000
pendapatan2 = 8000000

print(f"Pajak untuk pendapatan {pendapatan1}: Rp {hitung_pajak(pendapatan1):,.0f}")
print(f"Pajak untuk pendapatan {pendapatan2}: Rp {hitung_pajak(pendapatan2):,.0f}")

exit()

#------------------------Mencari Nilai Maksimum dalam List------------------------
def cari_maksimum(lst):
    return max(lst) #Mencari Nilai Minimum dalam List

def cari_minimum(lst):
    return min(lst) #Mengurutkan List dalam Urutan Ascending

def urut_asc(lst):
    return sorted(lst) #Mengurutkan List dalam Urutan Descending

def urut_desc(lst):
    return sorted(lst, reverse=True)

print(cari_maksimum([3, 1, 8, 2, 5]))  # Output: 8
print(cari_maksimum([10, 20, 5, 30, 25]))  # Output: 30

exit()

#------------------------Jumlahkan Digit dalam Bilangan------------------------
def jumlahkan_digit(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + jumlahkan_digit(n // 10) # Mengembalikan jumlah digit n dengan menambahkan digit terakhir (n % 10) dan hasil jumlah digit dari sisa bilangan (n // 10).

print(jumlahkan_digit(1234))
print(jumlahkan_digit(5678))

exit()


#------------------------Hitung Total Digit------------------------
def hitung_digit(n):
    if n == 0: # Jika n adalah 0, jumlah digitnya adalah 0
        return 0
    else:
        return 1 + hitung_digit(n // 10)  # Jika n lebih besar dari 0, tambahkan 1 dan panggil rekursi dengan n dibagi 10
    
print(hitung_digit(12345))
print(hitung_digit(987654))
exit()



#------------------------Buat fungsi rekursif untuk membalik string------------------------
def balik_string(teks):
    if len(teks) == 0:
        return teks
    else:
        return balik_string(teks[1:]) + teks[0]
print(balik_string("hello"))
exit()



#------------------------fungsi rekursif untuk menghitung jumlah angka dari 1 hingga n------------------------
def hitung_jumlah_angka(n):
    if n == 1:
        return 1 #Jika n sama dengan 1, fungsi mengembalikan 1. Ini mencegah rekursi berlanjut selamanya.
    else:
        return n + hitung_jumlah_angka(n-1) #Jika n lebih besar dari 1, fungsi mengembalikan nilai n ditambah hasil dari pemanggilan fungsi itu sendiri dengan argumen n - 1
    
n = 5
hasil = hitung_jumlah_angka(n)
print(hasil)

exit()


#------------------------Pangkat------------------------
def pangkat(a,b): #mendefinisikan sebuah fungsi bernama pangkat yang menerima dua argumen, yaitu a dan b
    return a ** b #mengembalikan hasil dari a dipangkatkan dengan b. Operator ** digunakan untuk menghitung pangkat
hasil = pangkat(2, 3) #memanggil fungsi pangkat dengan 2 sebagai a dan 3 sebagai b. Hasil dari fungsi ini (yaitu 2 ** 3, yang sama dengan 8) disimpan dalam variabel hasil
print(hasil)
