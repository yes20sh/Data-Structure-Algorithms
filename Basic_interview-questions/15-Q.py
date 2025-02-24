# 15 - Write a Python program to Merge Two Sorted Lists.
def sort_merge(lst1, lst2):
    lst=  sorted(lst1) + sorted(lst2)
    return sorted(lst)

lst1 = [1,23,7]
lst2 = [5,6,9,0]
print(f'Merged two sorted list : {sort_merge(lst1,lst2)}')