# 5 - Write a Python program to find Fibonacci Sequence.

def fibonacci_seq(nth):
    fibo_seq = [0,1]
    for i in range(2,nth):
        next_term = fibo_seq[-1] + fibo_seq[-2]  # Calculate the next term as the sum of the last two terms
        fibo_seq.append(next_term)
    return fibo_seq

nth = int(input("Enter the nth term : "))
print(f"The Fibonacci sequance up to {nth} terms : {fibonacci_seq(nth)}")


'''
The Fibonacci Sequence is a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. It appears in various natural phenomena and has applications in computer algorithms, mathematics, and financial models. The sequence begins as 0, 1, 1, 2, 3, 5, 8, etc

'''