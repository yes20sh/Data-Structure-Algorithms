# Question 2: Write a Python program to Check Palindrome.

def palindrome (str):
    str.replace(" ","").lower() 
    return str == str[::-1]

str = input("Input your string : ")
if not palindrome(str):
    print(str, "is not a palindrome")
else:
    print("It is a palindrome")

