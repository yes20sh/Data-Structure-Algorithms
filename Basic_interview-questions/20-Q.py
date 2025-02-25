# 20 - Write a Python program to Count Words in a Sentence.

def countword(sentance):
    words = sentance.split()
    return len(words)

# without using build-in function
def count_func(sentance):
    word_count = 0
    in_word = False
    for char in sentance:
        if char != " " and not in_word:
            word_count=+1
            in_word = True
        elif char == " " and in_word:
            in_word = False
    return word_count
        

sentance = input("Enter the sentence : ")
print(f"The sentance'{sentance} contains {countword(sentance)} words'")