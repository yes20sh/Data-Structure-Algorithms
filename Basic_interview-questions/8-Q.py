# 8. Write a Python program to find Prime Numbers.

def is_prime(num):
    if num < 1:
        return False
    for i in range(2, int(num** 0.5)+1):
        if num % i == 0:
            return False
    return True

def prime_numbers_seq(start,end):
    prime = []
    for n in range(start, end+1):
        if is_prime(n):
            prime.append(n)
    return prime

start, end = map(int, input("Enter the start and end term : ").split())

print(f"All Prime Number between {start} and {end} are {prime_numbers_seq(start, end)}")

'''
A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. 
In other words, it can only be divided evenly by 1 and the number itself.
Examples of prime numbers include 2, 3, 5, 7, 11, and 13
'''