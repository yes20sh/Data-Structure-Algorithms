# 19 - Write a Python program to check if a Number is Even or Odd.

def even_num(num):
    if num % 2 == 0:
        return 1
    return 0

num = int(input("Enter the number : "))
if even_num(num):
    print(f"{num} is a even number.")
else:
    print(f"{num} is not a even number.")

          
