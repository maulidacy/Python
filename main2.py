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