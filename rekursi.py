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
