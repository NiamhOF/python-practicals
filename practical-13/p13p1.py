'''

Practical 13, Exercise 1

Program to print largest of two numbers
Uses the function max
define max of a and b:
    if a is greater than b:
        return a
    else:
        return b

Ask user for two numbers defined as floats
define biggest as the function above assigned to the two numbers inputted
print the largest number

'''

def max(a, b):
    '''Function that returns the largest of its two arguements'''
    if a > b:
        return a
    else:
        return b

number1 = float (input ('Enter a number: '))
number2 = float (input ('Enter a number: '))

biggest = max(number1, number2)

print ('The largest number between', number1, 'and', number2, 'is', biggest)
