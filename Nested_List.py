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
#-------------------------------------------------------------------------------------------------------
