'''

Practical 13, Exercise 5

Program to illustrate scoping in Python

Define the function f of x:
    print in the function f
    define x as x times 5
    define y as 200
    define a as the string I'm in a function
    define b as 4 to the power of x
    print the values of x, y, z, a and b
    return x

define values for x, y, z, a and b
print the values of x, y, z, a and b before the function

define z as the function f(x)
print the values of x, y, z, a and b after this

'''

def f(x):
    '''Function that adds 1 to its argument and prints it out'''
    print ('In function f:')
    x *= 5
    y = 200
    a = "I'm in a function"
    b = 4 ** x
    print ('a is', a)
    print ('x is', x)
    print ('y is', y)
    print ('z is', z)
    print ('b is', b)
    return x

x, y, z, a, b = 5, 10, 15, 'Hello', 'Bye'

print ('Before function f:')
print ('a is', a)
print ('x is', x)
print ('y is', y)
print ('z is', z)
print ('b is', b)

z = f(x)

print ('After function f:')
print ('a is', a)
print ('x is', x)
print ('y is', y)
print ('z is', z)
print ('b is', b)

