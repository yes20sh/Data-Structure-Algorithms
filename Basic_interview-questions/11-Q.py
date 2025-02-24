# 11 - Write a Python program to calculate the Sum of Digits in a Number.

def sum_digit(num):
    sum_num = 0
    for n in num:
        sum_num += int(n)
    return sum_num

num = input("Enter the digits : ")
print(f"The sum of {num} digit numbers is {sum_digit(num)}")
