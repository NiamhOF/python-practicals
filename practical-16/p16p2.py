'''
Practical 16, Exercise 2

Define a function taking 2 numbers for evaluation
    for all the numbers in the range i from 1 up to the smallest number inputted
        if both numbers are divisible by the number with no remainder:
            divisors becomes a tuple that contains each of these numbers
    return divisors

Ask the user for two numbers
If the numbers are less than or equal to 0:
    print an error
else:
    divisors is assigned the return from passing the numbers into the function
    print the divisors

    define total as 0
    for all values in divisors:
        total becomes total + value
    return the sum of all the values of divisors         

'''

def findDiv (num1, num2):
    '''Finds the common divisors for num1 and num2
        Assumes num1 and num2 are positive integers
        Returns tuple containing the common divisors of num1 and num2'''

    divisors = ()
    for i in range (1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            divisors += (i, )
    return divisors

number1 = int(input ('Enter a positive integer: '))
number2 = int(input ('Enter another positive integer: '))

if number1 <= 0 or number2 <=0:
    print ('Numbers must be greater than zero')

else:
    divisors = findDiv (number1, number2)
    print ('The common divisors of:', number1, 'and', number2, 'are', divisors)

    total = 0
    for d in divisors:
        total += d

    print ('The sum of the common divisors is:', total)

print ('Finished')
