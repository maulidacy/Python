# Sistem Login dengan Batas Percobaan (While Loop) 
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
if kesempatan == 0:
    print("Maaf kesempatan habis. Akun terkunci!")
exit()

# Kalkulator Total Belanja (For Loop)
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