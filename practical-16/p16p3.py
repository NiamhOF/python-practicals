'''
Practical 16, Exercise 3

Define a funtion to check if number is perfect as isPerf
    Define add as 0
    for all values in the range i up to the specified number:
        if the number is divisable by the value of i with no remainder:
            assign add the value add plus i
        if add is equal to the number:
            it is a prime number
        else:
            is not a prime number
            
Define a function to print all the perfect numbers up to a limit
    define lis as a tuple
    for all values of i from 1 to the limit specified
        if the function isPerf returns True:
            add that value to the tuple lis.
    return lis

Ask user to input a number
print all the numbers in the range.

'''
def isPerf(n):
    """check if n is a perfect number"""
    add = 0
    for i in range(1, n):
        if (n % i == 0):
            add += i
    if add == n:
        return True
    else:
        return False
    
def allPerf(limit):
    """print all the perfect numbers up to limit"""
    lis = ()
    for i in range(1, limit):
        if isPerf(i):
            lis += (i, )
    return lis

num = int (input ('Enter a number: '))
print ('The list of perfect numbers up to', num, 'is', allPerf(num))



