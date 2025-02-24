# 13 - Write a Python program to check for Leap Year.

def leap_year(year):
    if (year % 4 == 0 and year % 100 != 0 )or (year % 400 == 0) :
        return 0
    return 1

year = int(input("Enter the year : "))
if leap_year(year):
    print(f"{year} is a leap year.")
else:
       print(f"{year} is not a leap year.")



'''
A leap year is a year that is divisible by 4, but if it is a century year (ending in 00), it must also be divisible by 400. Leap years have 366 days instead of the usual 365, with an extra day added to February, making it 29 days long.
'''