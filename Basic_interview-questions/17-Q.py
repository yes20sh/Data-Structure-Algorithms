# 17 - Write a Python program to Check for Perfect Numbers.

def is_perfect(numbers):
    num_perfect = 0
    for i in range(1,numbers):
        if numbers % i == 0:
            num_perfect += i
    return num_perfect == numbers

num = int(input("Enter the number: "))
if is_perfect(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")

    


'''
A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself. 
Proper divisors are all positive divisors of a number other than the number itself. 
For example, the number 6 is a perfect number because its divisors are 1, 2, and 3, and 1 + 2 + 3 = 6. 
Another example is 28, with divisors 1, 2, 4, 7, and 14, and 1 + 2 + 4 + 7 + 14 = 28. 
Perfect numbers are rare and have been studied for their unique properties and relationships to number theory.
'''