# 9 -  Write a Python program to check for Pangram.

def pangram(s):
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    s = s.replace(" ", "").lower()
    return set(s) >= alphabet

# example "The quick brown fox jumps over the lazy dog" : True
str = input("Enter the string : ")
if pangram(str):
    print("Yes, it is a pangram")
else:
    print("No, it is a pangram")



'''
A pangram is a sentence that contains every letter of the alphabet at least once. 
It is often used in testing typing skills, fonts, and keyboards. 
A well-known example is "The quick brown fox jumps over the lazy dog," which includes all 26 letters of the English alphabet.
'''




'''
A pangram is a sentence that contains every letter of the alphabet at least once. 
It is often used in testing typing skills, fonts, and keyboards. 
A well-known example is "The quick brown fox jumps over the lazy dog," which includes all 26 letters of the English alphabet.

'''