# 16 - Write a Python program to Remove Duplicates from a String.

def remove_duplicate(str):
    unique_element = set()
    result = ""
    for char in str:
        if char not in unique_element:
            result += char
            unique_element.add(char)
    return unique_element

str = input("Enter the string : ")
print(f"remove all duplicate in '{str}' and unique characters are : {remove_duplicate(str)}")