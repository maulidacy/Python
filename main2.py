#Konversi Suhu
print(20*"=")
print("Konversi Suhu")
print(20*"=" + "\n")

suhu = float(input("Masukkan suhu dalam Celcius: "))
fahrenheit = (suhu * 9/5) + 32
kelvin = suhu + 273.15

print(f"Dalam Fahrenheit: {fahrenheit}")
print(f"Dalam Kelvin: {kelvin}")

exit()