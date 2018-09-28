"""
Practical 6, Exercise 2

Ask the user for a number
Ask the user for another number
Ask the user for a third number
If number 1 is odd and greater than number 2 and 3, print number 1
If number 2 is odd and greater than number 1 and 3, print number 2
If number 3 is odd and greater than number 1 and 2, print number 3
Allow for if the some of the numbers are the same and have the highest value
If none of the number are odd, print 'None of these numbers are odd'
"""
number_1= int(input ("Enter a number: "))
number_2= int(input ("Enter another number: "))
number_3= int(input ("Enter a third number: "))

if number_1 % 2 != 0 and number_3 <= number_1 and number_1 >= number_2:
    print (number_1)
    
elif number_2 % 2 != 0 and number_1 <= number_2 and number_2 >= number_3:
    print (number_2)
    
elif number_3 % 2 != 0 and number_1 <= number_3 and number_3 >= number_2:
    print (number_3)
    
elif number_1 % 2 == 0 and number_2 % 2 == 0 and number_3 % 2 == 0:
    print ("None of these numbers are odd!")
