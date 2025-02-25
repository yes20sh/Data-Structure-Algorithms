# 22 Write a Python program to Find Second Largest Element in a List

def second_largest(lst):
    if len(lst) > 2:
        sorted_lst = sorted(lst)
        return sorted_lst[-2]
    else:
        return None

lst = list(map(int, input("Enter the list number : ").split()))
if second_largest(lst) is not None:
    print(f"The second largest number in list is {second_largest(lst)}")
else:
    print("List is less than 2 element, there is no 2nd largest number")


