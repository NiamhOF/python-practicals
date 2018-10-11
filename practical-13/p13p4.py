'''

Practical 13, Exercise 4

Program to illustrate scoping in Python

Define the function f of x:
    print in the function f
    define x as x + 1
    define y as 1
    print the values of x, y and z
    return x

define values for x, y and z
print the values of x, y and z before the function

define z as the function f(x)
print the values of x, y and z after this

'''

def f(x):
    '''Function that adds 1 to its arguement and prints it out'''
    print ('In function f:')
    x += 1
    y = 1
    print ('x is', x)
    print ('y is', y)
    print ('z is', z)
    return x

x, y, z = 5, 10, 15

print ('Before function f:')
print ('x is', x)
print ('y is', y)
print ('z is', z)

z = f(x)

print ('After function f:')
print ('x is', x)
print ('y is', y)
print ('z is', z)
