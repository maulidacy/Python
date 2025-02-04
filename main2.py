

# Hitung Jumlah Huruf dalam Kalimat
print(33*"=")
print("Hitung Jumlah Huruf dalam Kalimat")
print(33*"=" + "\n")

kalimat = input("Masukkan kalimat: ")
huruf = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
jumlah_huruf = 0

for i in  huruf:
    jumlah_huruf += kalimat.count(i)
print(f"Jumlah huruf: {jumlah_huruf}")

exit()


# Mengecek Kata Palindrom 
print(23*"=")
print("Mengecek Kata Palindrom")
print(23*"=" + "\n")

kata = input("Masukkan kata: ")

kata_asli = kata # Membuat variabel untuk menyimpan kata yang diinputkan
kata_balik = kata[::-1] # Membuat variabel untuk menyimpan kata yang diinputkan dalam bentuk huruf kebelakang

# Membuat perbandingan antara kata asli dan kata yang diinputkan dalam bentuk huruf ke belakang
if kata == kata_balik:
    print(f"{kata_asli} adalah kata palindrom.")
else:
    print(f"{kata_asli} bukan kata palindrom.")
exit()




# Menghitung Rata-rata Nilai
print(25*"=")
print("Menghitung Rata-rata Nilai")
print(25*"=" + "\n")

n = int(input("Masukkan jumlah mata pelajaran: "))
total_nilai = 0

# Looping untuk meminta input nilai setiap mata pelajaran
for i in range(n):
    nilai = float(input(f"Masukkan nilai ke-{i + 1}: "))
    total_nilai += nilai
    rata_rata = total_nilai / n
print(f"Rata-rata nilai: {rata_rata}")

exit()


# Kalkulator Diskon
print(20*"=")
print("Kalkulator Diskon")
print(20*"=" + "\n")

harga_barang = float(input("Masukkan harga barang: "))
diskon = float(input("Masukkan persentase diskon: "))

jumlah_diskon = (diskon / 100) * harga_barang
harga_setelah_diskon = harga_barang - jumlah_diskon

print(f"Harga setelah diskon: {harga_setelah_diskon}")
exit()


# Konversi Suhu
print(20*"=")
print("Konversi Suhu")
print(20*"=" + "\n")

suhu = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = (suhu * 9/5) + 32
kelvin = suhu + 273.15

print(f"Dalam Fahrenheit: {fahrenheit}")
print(f"Dalam Kelvin: {kelvin}")

exit()