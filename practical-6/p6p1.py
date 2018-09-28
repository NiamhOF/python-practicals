"""
Practical 6, exercise 1

Ask the user to input an integer
Ask the user to input another integer
Add the two integers
If the sum of the integers in greater than 100 print 'That is a big number'
If equal to 100, tell user
If it is smaller than 100, print 'That number is less than 100'

"""

number_1 = int(input ("Enter a number: "))
number_2 = int(input ("Enter another number: "))
total = number_1 + number_2

if total > 100:
    print ("That is a big number")

elif total == 100:
    print ("Those numbers are equal to 100")

else:
    print ("That number is less than 100")
