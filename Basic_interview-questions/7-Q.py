# 7 - Write a Python program to find Anagram Check.

# approach 1
def anagram(str1, str2):
    str1.replace(" ","").lower()
    str2.replace(" ","").lower()
    for char in str1:
        if char not in str2:
            return 1
    return 0

# approach 2 : with inbuild functiom
def anagram_fun(str1, str2):
    str1.replace(" ","").lower()
    str2.replace(" ","").lower()
    return sorted(str1) == sorted(str2)

str1, str2 = input("Enter your both words :  ").split()
if anagram(str1, str2):
    print(f"your words are '{str1}' and '{str2}' is not anagram")
else:
    print(f"your words are '{str1}' and '{str2}' is anagram")



'''
Hint

An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once. For example, "listen" and "silent" are anagrams of each other. Anagrams are often used in word games and puzzles.

'''