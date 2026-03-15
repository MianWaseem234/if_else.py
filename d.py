num = int(input("Enter number: "))
binary = ""

while num > 0:
    binary = str(num % 2) + binary
    num //= 2

print("Binary:", binary)