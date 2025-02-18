#------------------------Melewati Huruf Vokal dalam Kata------------------------
huruf_vokal = "aiueoAIUEO"
kata = input("Masukkan kata: ")
hasil = ""

for huruf in kata:
    if huruf in huruf_vokal:
        continue
    hasil += huruf # Menambahkan huruf ke hasil jika bukan vokal
print("Kata tanpa huruf vokal: ", hasil)
exit()


#------------------------Melewati Bilangan Genap------------------------
for angka in range(1, 11):
    if angka % 2 == 0:
        continue #akan melewati angka genap
    print("Angka: ", angka)
exit()


#------------------------Melewati Angka Tertentu------------------------
for angka in range(1, 11):
    if angka == 5:
        continue #akan melewati angka 5
    print("Angka: ", angka)