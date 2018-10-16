'''

Practical 14, Exercise 1

Program to get the factorial of a number

(a) define the function fact (x)
    if x is 0
        return 1
    else:
        return x times the function of fact (x - 1)

(b) ask the user for a number
    if the number is less than zero:
        print an error
    else:
        print the factorial as the function fact of the number entered

'''

def fact (x):
    
    '''Function that returns the factorial of argument using recursion.
    Assumes a non-negative integer'''
    
    if x == 0:
        return 1
    else:
        res = x * fact (x - 1)
        return res
            

num = int (input ('Enter a positive number to get the factorial: '))

while num >= 0:
    print ('The factorial of', num, 'is', fact(num))
    num = int (input ('Enter a positive number to get the factorial: '))
    
if num < 0:
    print ('Error, that number is less than zero')
    
