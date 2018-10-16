'''
Practical 14, Exercise 1

Ask user for a number
while the number is greater than or equal to 0
    if the number is 0, the factorial is 1
    if the number is 1, the factorial is 1
    if the number is greater than 1:
        define fact as 1
        for all numbers i of the integers from 1 to number
            fact is fact times i
    tell the user the factorial
    ask for another number
if the number is less than 0, tell the user

'''

num = int (input ('Enter a positive integer: '))

while num >= 0:
    if num == 0:
        fact = 1
    elif num == 1:
        fact = 1
    else:
        fact = 1
        i = 1
        while i <= num:
            fact *= i
            i += 1

    print ('The factorial of', num, 'is', fact)
    num = int (input ('Enter a positive integer: '))

if num < 0:
    print ('Number entered was less than 0')
