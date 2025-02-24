# 4 - Write a Python program to find Factorial with Recursion.

def factorial (num):
    if num == 0:
        return 1
    return num * factorial(num - 1)

num = int(input("Enter the number : "))
print(f"Factorial of {num} is {factorial(num)} ")

'''
Factorial of a non-negative integer is the product of all positive integers less than or equal to that integer. It is denoted by n! and is used in permutations, combinations, and other mathematical calculations. For example, 5! = 5 × 4 × 3 × 2 × 1 = 120.

'''