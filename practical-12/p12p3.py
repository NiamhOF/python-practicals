'''

Practical 12, Exercise 3

(a) Define the function root with the two values of epsilon and number
        Define step as epsilon squared
        define root as 0.0
        while the absolute value of the number minus the root squared and root is less than or equal to number
            define root as root plus step
            if the absolute value of number minus root squared is less than epsilon
                return root
                
(b) ask user to input a number to be used in function as num
define epsilon as 0.01 to be used in function as epsilon
print the approximate square root

'''

def root(ep, num):
    step = ep ** 2
    root = 0.0
    while abs (num - root ** 2) >= ep and root ** 2 <= num:
        root += step
    if abs (num - root ** 2) < ep:
        return root
    else:
        return 'No square root found'

number = float (input ('Enter a number to calculate the square root: '))
epsilon = 0.01
print ('The approximate square root of', number, 'is', root(epsilon, number))
