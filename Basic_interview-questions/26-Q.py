# 26 - Write a Python program to convert Celsius to Fahrenheit.

def convert_cel_Feh(cel):
    fahrenheit = (cel*9/5) + 32
    return fahrenheit

celsius = float(input("Enter the celsius : "))
print(f'{celsius} celsius as fahrenheit {convert_cel_Feh(celsius):.1f}')