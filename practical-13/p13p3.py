'''

Practical 13, Exercise 3

Program to print the largest of two user entered numbers

define the function print_max

    within this function defint max of two numbers a and b:
        if a is greater than b:
            return a
        else:
            return b

    ask the user for two numbers
    print the largest using the max function
    return

use the function print_max to print the answer

'''

def print_max():
    '''Function prints the lagest of two numbers'''

    def max(a, b):
        '''Function return the largest of its two arguements'''
        if a > b:
            return a
        else:
            return b
        
    number1 = float(input ('Enter a number: '))
    number2 = float(input ('Enter a number: '))
    print ('The largest number between', number1, 'and', number2, 'is', max(number1, number2))

    return

print_max()
