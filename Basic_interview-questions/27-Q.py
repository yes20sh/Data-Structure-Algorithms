# 27 - Write a Python program to calculate the LCM (Least Common Multiple) of Two Numbers.

import math

def lcm(num1, num2):
    return abs(num1 * num2) // math.gcd(num1, num2)

num1, num2 = map(int, input("Enter the two number for LCM : ").split())
print("The LCM of", num1, "and", num2, "is", lcm(num1, num2))
