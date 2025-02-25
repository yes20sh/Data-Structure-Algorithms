# 23 Write a Python program to Reverse Words in a String.

def reverse_words(str):
    words = str.split()
    reverse_word = words[::-1]
    reverse_string = " ".join(reverse_word)
    return reverse_string

str = input("Enter the string : ")
print(f"Real string : {str}")
print(f"Reverse String : {reverse_words(str)}")