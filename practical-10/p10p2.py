'''

Practical 10, Exercise 2

ask user to enter a number, assign this to number
while the number is not equal to 0
    assign cube the value 0
    while cube cubed is less than the absolute value of number:
        cube equale cube plus 1
    if the cube cubed is equal to the absolute value of the number:
        if the number is less than zero
            positive cube becomes negative cube
        print the cube root
    else:
        print that the number is not a perfect cube
    ask the user for another number
if the number is zero. Tell the user and finish the program.

'''

number = int (input('Enter a number to calculate the cube root: '))

while number != 0:
    cube = 0
    while cube ** 3 < abs(number):
        cube += 1

    if cube ** 3 == abs(number):
        if number < 0:
            cube = -cube
        print ('Cube root of', number, 'is', cube)

    else:
        print (number, 'is not a perfect cube')
    number = int (input('Enter a number to calculate the cube root: '))

print ('Number is equal to zero. Program finished.')
