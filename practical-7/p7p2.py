"""
Practical 7, Exercise 2

Ask user for a year
If the year is not evenly divisible by 4 it is a common year
Else
if the year is not evenly divisible by 100 then it is a leap year
Else
if the year is not divisible by 400 then it is a common year
else
it is a leap year
Tell user of result

"""

year = int(input ("Enter a year: "))

if year % 4 != 0:
    print (year, "is a common year")
elif year % 100 != 0:
    print (year, "is a leap year")
elif year % 400 != 0:
    print (year, "is a common year")
else:
    print (year, "is a leap year")
