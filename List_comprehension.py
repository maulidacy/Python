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