# 14 - Write a Python program to find the Average Numbers in a List.

def average_number(lst):
    if not lst:
        return None
    total_num = sum(lst)
    average = total_num / len(lst)
    return average

lst_num = list(map(int, input("Enter the numbers : ").split()))
print(f"Average of '{lst_num}' is {average_number(lst_num):.2f}")

