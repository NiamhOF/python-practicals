'''

Practical 14, Exercise 4

Program to get prime numbers in a range of integers.

Define the function isPrime:
    define isPrime (number) as true
    for all numbers in the range i from 2 up to number:
        if the number is divisable by i with no remainder
            isPrime is false
            print the number and the factors of that number
    return isPrime

For number in the range of 2 up to 20:
    if the function isPrime is true:
        print the number is prime

print finished

'''

def isPrime (number):
    '''Function to get prime numbers in a range'''
    isPrime = True
    for i in range (2, number):
        if number % i == 0:
            isPrime = False
            print (number, 'equals', i, '*', number//i)
    return isPrime

for number in range (2, 20):
    if isPrime(number):
        print (number, 'is a prime number')

print ('Finished!')
