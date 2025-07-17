#------------------------- 4. Cetak segitiga bintang -------------------------
n = int(input("Masukkan n: "))
for i in range(1, n + 1):
    print('*' * i)  # Mencetak bintang sebanyak i kali, menghasilkan pola segitiga.
exit()

#------------------------- 3. Hitung jumlah bilangan dari 1 sampai 100 -------------------------
jumlahBilangan = 0
n = 100

for i in range(1, n + 1):
    jumlahBilangan += i
    print(f"Jumlah: {jumlahBilangan}")
exit()

#------------------------- 2. Tampilkan angka genap dari 1 sampai 20 -------------------------
jumlah_genap = 0
print("Angka genap:", end=" ")
n = 20  # batas atas

for i in range(1, n + 1): # Loop dari angka 1 sampai 20 (range(1, 21), karena n + 1 = 21 → akhir range tidak termasuk).
    if i % 2 == 0:
        print(i, end=" ") # Mencetak tulisan "Angka genap:" di awal baris, tanpa ganti baris (end=" ").
        jumlah_genap += 1

print()
print("Jumlah angka genap:", jumlah_genap)
exit()

#------------------------- 1. Cetak angka 1 sampai 10 -------------------------
for i in range(1, 11):
    print(i)