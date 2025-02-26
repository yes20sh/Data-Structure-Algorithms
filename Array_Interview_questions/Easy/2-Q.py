# 2 Find the Third Largest Number in an Array

def third_largest(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst) > 3:
        return sorted_lst[-3]
    elif len(sorted_lst) == 3:
        return sorted_lst[0]
    else:
        return 0
    
lst = list(map(int, input("Enter list of element : ").split()))
if third_largest(lst):
     print(f"The 3nd largest element in list is {third_largest(lst)}")
else:
    print("There is no 3nd largest element, list have less than 3 element")