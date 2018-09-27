"""
Practical 7, Exercise 1

Ask user for a year
Read year
If the year is greater than 0 then
    if (it is divisable by 4 and not evenly divisable by 100)
        or if the year is evenly divisable by 400 then
            Print that 'It is a leap year'
    else if the above are false, print 'It is not a leap year'
else
    Tell user the year must be greater than 0

"""

year = int(input ("Enter a year: "))

if year > 0:  
    if (year % 4 == 0 and year % 100 !=0) or year % 400 == 0:
        print (year, "is a leap year.")
    else:
        print (year, "is not a leap year.")

else:
        print ("Year must be greater than 0")
