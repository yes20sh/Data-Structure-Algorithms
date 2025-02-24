# 3: Write a Python program to Count Vowels in a String.

def count_vowels(str):
    str.replace(" ","").lower
    vowels = "aeiou"
    count = 0
    for char in str:
        if char in vowels:
            count +=1
    return count

str = input("Enter your string : ")
print("Total vowels present in your string : ", count_vowels(str))

