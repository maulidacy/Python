#--------------------------------------Menghitung Total Pendapatan----------------------------------------
produk = [
    ["Sepatu", 600000, 10],
    ["Baju", 230000, 20],
    ["Kacamata", 750000, 5]
]

total = 0
for i in range(len(produk)):
    total += produk[i][1] * produk[i][2]
print(f"Total pendapatan: {total}")

#versi comprehension
total = sum([harga * jumlah for _, harga, jumlah in produk])
# for _, harga, jumlah in produk → langsung unpack elemen nested list.
# _ → nama produk (pakai _ artinya abaikan nilainya).
# harga * jumlah → hitung pendapatan per produk.
# sum([...]) → jumlahkan semua pendapatan.
print(f"Total pendapatan: {total}")

# versi lebih clean lagi tanpa tanda [] (pakai generator expression)
total = sum(harga * jumlah for _, harga, jumlah in produk)
print(f"Total pendapatan: {total}")
#-------------------------------------------------------------------------------------------------------
