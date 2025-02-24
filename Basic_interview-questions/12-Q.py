# 12 - Write a Python program to check for Armstrong Number.

def arnstrong_number (digit):
    arm_num = 0
    for num in digit:
        arm_num = arm_num + int(num)**3
    return int(digit) == arm_num

digit = input("Enter the digit : ")
if arnstrong_number(digit):
    print(f"Yes, {digit} is an Armstrong Number.")
else:
    print(f"No, {digit} is not an Armstrong Number.")



'''
An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits. 
For example, 153 is an Armstrong number because 1³ + 5³ + 3³ = 153.
'''