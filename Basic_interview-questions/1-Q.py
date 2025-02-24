#  Question 1 : Write a Python program to Reverse a String.

def reverse_string(str):
    return str[::-1]

str = input("Enter your string : ")
print("Your string : ", str)
print("your reverse string : ", reverse_string(str))
