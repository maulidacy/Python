#-----------------------------------------------------------------
try:
    pembilang = int(input("Masukkan pembilang: "))
    penyebut = int(input("Masukkan penyebut: "))
    hasil = pembilang / penyebut
    print(f"Hasil pembagian: {hasil}")
except ZeroDivisionError:
    print("Penyebut tidak boleh nol!")
exit()

#-----------------------------------------------------------------
try:
    angka = int(input("Masukkan angka: "))
except ValueError:
    print("Input harus berupa angka!")
#-----------------------------------------------------------------
