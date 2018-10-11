'''

Practical 13, Exercise 6

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

(c)

'''

def fact (x):
    if x == 0:
        return 1
    else:
        print ('The number now being evaluated is:', x, '. The factorial of this is', x * fact(x -1))
        return x * fact (x - 1)
            

num = int (input ('Enter a positive number to get the factorial: '))

if num < 0:
    print ('Error, that number is less than zero')
    
else:
    print ('The factorial of', num, 'is', fact(num))
