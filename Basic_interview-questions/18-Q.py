# 18 - Write a Python program to Find the Maximum Difference between Two Elements in a List.

def max_difference(lst1, lst2):
   difference = max(lst1) - max(lst2)
   return difference

lst1 = [3,7,5,13,5]
lst2 = [9,5,2,10,15,23]
print(max_difference(lst1, lst2))