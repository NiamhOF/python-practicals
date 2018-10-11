'''

Practical 10, Exercise 1

Ask user for a number
Assign square_root the value 0
while number is greater than or equal to 0:
    while the square_root squared is less than the value of the number
        assign square_root the value sqaure_root + 1
    if the square_root squared is equal to the value of the number
        print the square root
    else:
        print that the number is not a perfect square
    ask the user for another number while a number is not negativw.
if the number is less than 0. Note this and finish program

'''

number = int(input('Enter the number you want to find the square root of: '))

square_root = 0
    
while number >= 0:
    while square_root**2 < number:
        square_root += 1

    if square_root**2 == number:
        print ('Square root of', number, 'is', square_root)

    else:
        print (number, 'is not a perfect square')

    square_root = 0

    number = int(input('Enter the number you want to find the square root of: '))
print ('Number is negative. Program finished.')
