# Cek Angka Ganjil atau Genap
print(35*"=")
print("Cek Angka Ganjil atau Genap")
print(35*"=" + "\n")

angka = float(input("Masukkan sebuah angka: "))

if angka % 2 == 0:
    print("Angka tersebut adalah genap.")
else:
    print("Angka tersebut adalah ganjil.")
exit()

# Cek Bilangan Positif, Negatif, atau Nol
print(40*"=")
print("Cek Bilangan Positif, Negatif, atau Nol")
print(40*"=" + "\n")

angka = float(input("Masukkan sebuah angka: "))

if angka > 0:
    print("Angka tersebut adalah positif.")
elif angka < 0:
    print("Angka tersebut adalah negatif.")
else:
    print("Angka tersebut adalah nol.")

exit()


# Operasi Aritmatika Sederhana
print(28*"=")
print("Operasi Aritmatika Sederhana")
print(28*"=" + "\n")

angka_1 = float(input("Masukkan angka pertama: "))
angka_2 = float(input("Masukkan angka kedua: "))
print(f"Penjumlahan: {angka_1 + angka_2}")
print(f"Pengurangan: {angka_1 - angka_2}")
print(f"Perkalian: {angka_1 * angka_2}")
print(f"Pembagian: {angka_1 / angka_2}")

exit()



# Hitung Luas Lingkaran
print(20*"=")
print("Hitung Luas Lingkaran")
print(20*"=" + "\n")

r = float(input("Masukkan jari-jari lingkaran : "))
luas = 3.14 * (r * r)

print(f"Luas lingkaran adalah: {luas}")
exit()



# Deklarasi Variabel
print(20*"=")
print("Deklarasi Variabel")
print(20*"=" + "\n")

angka_bulat = int(input("Angka bulat: "))
print(type(angka_bulat))

angka_pecahan = float(input("Angka pecahan: "))
print(type(angka_pecahan))

teks = input("Teks: ")
print(type(teks))

boolean = bool(input("True/False: "))
print(type(boolean))

input_list = list(input("List: "))
print(type(input_list))

exit()
