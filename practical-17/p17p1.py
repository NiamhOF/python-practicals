'''
Practical 17, Exercise 1

Define a function findDiv
    start the tuple divisors with the number 1 in it
    for all numbers in a range from 2 to half of the number plus 1
        if the number is divisible by the value of i with no remainder:
            add that value of i to the tuple divisors
    return divisors

Ask user to input a number

if the number is less than zero:
    give an error

else:
    print the divisors using the function findDiv

'''
def findDiv (num):
    '''Number to find the divisors of a number'''
    divisors = (1, )
    for i in range (2, num//2 + 1):
        if num % i == 0:
            divisors += (i, )
    return divisors

num = int (input ('Enter a positive integer: '))

if num <= 0:
    print ('Number needs to be a positive integer')

else:
    print ('The divisors of', num, 'are', findDiv(num))

    
