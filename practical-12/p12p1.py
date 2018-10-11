'''

Practical 12, Exercise 1

(a) define function as:
    for the factoiral of number
    take fact as 1
    for all numbers in the range i up to the number + 1
        fact is fact times each number in i
    return the factorial as fact

(b) ask user to input a number:
if the number is less than 0:
    print an error
else:
    print the factorial as function fact of the number entered.

'''

def fact(a):
    fact = 1
    for i in range (1, a + 1):
        fact *= i
    return fact

num = int (input ('Enter a non-negative number to get the factorial: '))
if num < 0:
    print ('Error. Number must be 0 or greater')
else:
    print ('The factorial of', num, 'is', fact(num))
