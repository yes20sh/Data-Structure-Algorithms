# 10 - Write a Python program to find the Minimum Element in a List.

# approch 1 : using inbuild function
def min_func(lst):
    return min(lst)

# approch 2
def min_sort (lst):
    sorted_lst = sorted(lst)
    return sorted_lst[0]

# approch 3
def min_for (lst):
    min_num = lst[0]
    for n in lst:
        if n < min_num:
            min_num = n
    return min_num


lst = list(map(int, input("Enter your list of numbers : ").split()))
print(f"Your list : {lst}")
print(f"Maximum element in a list : {min_func(lst)}")
print(f" approach 1 : {min_sort(lst)}")
print(f" approach 2 : {min_for(lst)}")

