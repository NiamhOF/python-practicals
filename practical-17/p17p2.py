'''
Practical 17, Exercise 2

Define a function findDiv passing two numbers in
    if the smaller of the numbers divides into to larger number with no remainder:
    divisors is the tuple (1, min number)
    else:
    start the tuple divisors with the number 1 in it
    for all numbers in a range from 2 to half of the smaller number plus 1
        if the number 1 is divisible by the value of i with no remainder and
        number 2 is divisible by the value of i with no remainder:
            add that value of i to the tuple divisors
    return divisors

Ask user to input a number

if either of the numbers are less than zero:
    give an error

else:
    print the divisors using the function findDiv

'''
def findDiv (num1, num2):
    '''Number to find the divisors of two numbers'''
    if max(num1, num2) % min(num1, num2) == 0:
        x = min (num1, num2)
        divisors = (1, x)
    else: 
        divisors = (1, )
    for i in range (2, min(num1, num2)//2 + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i, )
    return sorted(divisors)

num1 = int (input ('Enter a positive integer: '))
num2 = int (input ('Enter a positive integer: '))

if num1 <= 0 or num2 <= 0:
    print ('Number needs to be a positive integer')

else:
    print ('The divisors of', num1, 'and', num2, 'are', findDiv(num1, num2))
