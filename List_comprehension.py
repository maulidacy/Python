#-------------------------------Filter Nama Pendek-------------------------------
nama = ["Ayu", "Budi", "Putri", "Dian", "Salman", "Rian"]
new_nama = []

for i in nama:
    panjang = len(i)
    if panjang < 5:
        new_nama.append(i)
print(new_nama)

#Versi List Comprehension
new_nama_com = [i for i in nama if len(i) < 5]
print(new_nama_com)
exit()

#-------------------------------Ganda Tiga atau Ganjil-------------------------------
angka = list(range(1, 21))
hasil = []

for i in angka:
    if i % 3 == 0:
        hasil.append("Fizz")
    elif i % 2 != 0:
        hasil.append("Ganjil")
print("\nList biasa: ", hasil)

#Versi List Comprehension
hasil = ["Fizz" if i % 3 == 0 else "Ganjil"
         for i in angka if i % 3 == 0 or i % 2 != 0]
print("\nList Comprehension: ", hasil)

exit()

#------------------------------Kuadrat List-----------------------------
def kuadrat_list(data):
    return [i**2 for i in data]

# Contoh penggunaan:
data = [1, 2, 3, 4, 5]
print(kuadrat_list(data))
#----------------------------------------------------------------------