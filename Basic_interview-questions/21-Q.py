# 21 Write a Python program to Convert Decimal to Binary.

def decimal_binary(decimal):
    binary = " "
    quotient  = decimal
    while quotient < 0:
        reminder = quotient / 2
        binary = str(reminder) + binary
        quotient //= 2
    return binary

decimal = int(input("Enter the number : "))
print(f"{decimal} decimal number converted {decimal_binary(decimal)} binary number.")
