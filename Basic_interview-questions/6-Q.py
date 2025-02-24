# 6 - Write a Python program to find the Maximum Element in a List.

# function I
def maximum_func(lst):
    return max(lst)

# function II
def maximum(lst):
    max_num = lst[0]
    for n in lst:
        if n >= max_num:
            max_num = n
    return max_num

lst = list(map(int,input("Enter the numbers: ").split()))
print(f"The list of numbers : {lst}")
print(f"Maximum element in list : {maximum_func(lst)}")

