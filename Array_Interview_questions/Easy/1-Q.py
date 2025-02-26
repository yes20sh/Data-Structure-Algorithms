# 1 - Find the Second Largest Number in an Array

def second_largest(lst):
    shorted_lst = sorted(lst)
    if len(shorted_lst) == 2:
        return shorted_lst[0]
    elif len(shorted_lst) > 2 :
        return shorted_lst[-2]
    else:
        return 0

lst = list(map(int, input("Enter the number : ").split()))
if second_largest(lst):
    print(f"The 2nd largest element in list is {second_largest(lst)}")
else:
    print("There is no 2nd largest element, list have less than 2 element")
