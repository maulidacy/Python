#-----------------------------------------------------------------
while True:
    try:
        number = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
exit()

#-----------------------------------------------------------------
try:
    numerator = int(input("Enter the numerator: ")) #pembilang
    denominator = int(input("Enter the denominator: ")) #penyebut
    results = numerator / denominator
    print(f"Division results: {results}") #pembagian
except ZeroDivisionError:
    print("The denominator cannot be zero!")
exit()

#-----------------------------------------------------------------
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
#-----------------------------------------------------------------
