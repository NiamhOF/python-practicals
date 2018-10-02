'''
Practical 9, Exercise 3

Ask user for a number
If the number is less than 0, tell the user and exit
else
    if the number is 0, the factorial is 1
    if the number is 1, the factorial is 1
    if the number is greater than 1:
        define fact as 1
        for all numbers i of the integers from 1 to number
            fact is fact times i
    tell the user the factorial and exit

'''

num = int (input ('Enter a positive integer: '))

if num < 0:
    print ('Number entered was less than 0')

else:
    if num == 0:
        fact = 1
    elif num == 1:
        fact = 1
    else:
        fact = 1
        for i in range (1, num + 1):
            fact *= i

    print ('The factorial of', num, 'is', fact)
