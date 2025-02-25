# 25 Write a Python program to check if a Number is a Power of Two.

def is_power(num):
    if num < 0:
        return False
    while num > 1:
        if num % 2 != 0:
            return False
        num //= 2
    return True

num = int(input("Enter the number : "))
if is_power(num):
    print(f"{num} is power of 2")
else:
    print(f"{num} is not power of 2")
