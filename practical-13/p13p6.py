'''

Practical 13, Exercise 6

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

(c) add print statements to the function to show the recursion working
    print current number
    print factorial of that number

'''

def fact (x):
    
    '''Function that returns the factorial of argument using recursion.
    Assumes a non-negative integer'''
    
    if x == 0:
        return 1
    else:
        res = x * fact (x - 1)
        print ('The number now being evaluated is:', x)
        print ('The current factorial is:', res)
        return x * fact (x - 1)
            

num = int (input ('Enter a positive number to get the factorial: '))

if num < 0:
    print ('Error, that number is less than zero')
    
else:
    print ('The factorial of', num, 'is', fact(num))
