print("This program will check whether the entered year is leap year or not.")
year = int(input("Enter the year in format YYYY: "))

"""
Every year that is exactly divisible by four is a leap year, except for years that are exactly divisible by 100, 
but these centurial years are leap years if they are exactly divisible by 400. 
For example, the years 1700, 1800, and 1900 are not leap years, but the years 1600 and 2000 are.
Reference: https://en.wikipedia.org/wiki/Leap_year#:~:text=Every%20year%20that%20is%20exactly,years%201600%20and%202000%20are.
"""

# Condition 1: If a year is divisible by 4, it's a leap year.
# Condition 2: However, if the year is also divisible by 100, it is not a leap year unless:
# Condition 3: The year is divisible by 400, in which case it is a leap year.

leap_year = False

if year % 4 == 0:
    leap_year = True
    if year % 100 == 0:
        leap_year = False
        if year % 400 == 0:
            leap_year = True

if leap_year:
    print(f"The given year {year} is a leap year.")
else:
    print(f"The given year {year} is NOT a leap year.")    
