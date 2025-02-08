#-------------------------Konversi Suhu (For Loop)-------------------------
print(15*"=")
print("Konversi Suhu")
print(15*"=" + "\n")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

jumlah_suhu = int(input("Masukkan jumlah suhu: "))

suhu_list = [] # Menyimpan suhu yang dimasukkan
for i in range(jumlah_suhu):
    suhu = float(input(f"Masukkan suhu ke-{i + 1} (C): "))
    suhu_list.append(suhu) # menambahkan nilai suhu yang dimasukkan oleh pengguna ke dalam daftar suhu_list.

print("\nHasil konversi:")
for suhu in suhu_list:
    fahrenheit = celsius_to_fahrenheit(suhu)
    print(f"{int(suhu)}C = {int(fahrenheit)}F")
exit()


#-------------------------Mesin Parkir (While Loop)-------------------------
print(15*"=")
print("Mesin Parkir")
print(15*"=" + "\n")

tarif_per_jam = 5000
biaya_parkir = 0
total_pembayaran = 0

while True:
    jumlah_jam = float(input("Masukkan jumlah jam parkir: "))
    biaya_parkir = jumlah_jam * tarif_per_jam
    total_pembayaran += biaya_parkir
    print(f"Biaya parkir: Rp {biaya_parkir}")
    perintah = input("Ketik 'keluar' untuk berhenti atau tekan enter untuk lanjut: ")
    if perintah.lower() == "keluar": #lower() digunakan untuk mengubah semua huruf dalam string menjadi huruf kecil.
        print(f"Total pembayaran: {total_pembayaran}")
        break
exit()


#-------------------------Menghitung Rata-rata Nilai Siswa (For Loop)-------------------------
print(35*"=")
print("Menghitung Rata-rata Nilai Siswa")
print(35*"=" + "\n")

jumlah_siswa = int(input("Masukkan jumlah siswa: "))
total_nilai = 0

for i in range(jumlah_siswa):
    nilai = float(input(f"Masukkan nilai siswa ke-{i + 1}: "))
    total_nilai += nilai
    rata_rata = total_nilai / jumlah_siswa
print(f"Rata-rata nilai kelas: {rata_rata}")

exit()


#-------------------------Sistem Login dengan Batas Percobaan (While Loop)-------------------------
print(35*"=")
print("Sistem Login dengan Batas Percobaan")
print(35*"=" + "\n")

username = "admin"
password = 1234
input_username = input("Masukkan username: ")
kesempatan = 3


while kesempatan > 0:
    input_password = input("Masukkan password: ")
    if input_username == username and input_password == str(password):
        print("Login berhasil! Selamat datang.")
        break
    elif input_username == username and input_password != password:
        kesempatan -= 1
        print(f"Password salah! {kesempatan} percobaan tersisa.")
if kesempatan == 0: # Memeriksa apakah kesempatan telah habis.
    print("Maaf kesempatan habis. Akun terkunci!")
exit()


#-------------------------Kalkulator Total Belanja (For Loop)-------------------------
print(25*"=")
print("Kalkulator Total Belanja")
print(25*"=" + "\n")

jumlah_barang = int(input("Masukkan jumlah barang: "))
total_harga = 0

for i in range(jumlah_barang):
    harga = int(input(f"Masukkan harga barang ke-{i + 1}: "))
    total_harga += harga
print(f"Total harga belanjaan: {total_harga}")

exit()