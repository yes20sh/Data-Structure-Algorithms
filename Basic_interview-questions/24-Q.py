# 24 - Write a Python program to check if a Number is a Prime Factor.

def is_prime_factor(number, potential_factor):
    if number <= 1 or potential_factor <= 1:
        return False  # Numbers less than or equal to 1 are not considered prime factors
    return number % potential_factor == 0

# Example usage
number = 15
potential_factor = 3
if is_prime_factor(number, potential_factor):
    print(potential_factor, "is a prime factor of", number)
else:
    print(potential_factor, "is not a prime factor of", number)


'''
A prime factor is a factor of a number that is a prime number. 
In other words, it is a prime number that divides another number exactly, without leaving a remainder. 
For example, the prime factors of 28 are 2 and 7, because 2 and 7 are prime numbers and 28 can be divided by 2 and 7 without leaving a remainder (28 = 2 × 2 × 7). 
Prime factors are important in number theory and are used in various mathematical applications, including cryptography and the simplification of fractions.

'''