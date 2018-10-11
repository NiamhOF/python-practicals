'''

Practical 13, Exercise 5

Program to illustrate scoping in Python

Define the function f of c:
    print in the function f
    define a as the string Hello
    define c as the string after
    define e as 20
    print the values of a, b, c, d and e
    return c

define values for a, b, c, d and e
print the values of a, b, c, d and e before the function

define c as the function f(c)
print the values of a, b, c, d and e after this

'''

def f(c):
    '''Function that its arguement to a string and prints it out'''
    print ('In function f:')
    a = "Hello"
    c = "after"
    e = 20
    print ('a is', a)
    print ('b is', b)
    print ('c is', c)
    print ('d is', d)
    print ('e is', e)
    return c

a, b, c, d, e = "This", "is", "without", "the", "function"

print ('Before function f:')
print ('a is', a)
print ('b is', b)
print ('c is', c)
print ('d is', d)
print ('e is', e)

c = f(c)

print ('After function f:')
print ('a is', a)
print ('b is', b)
print ('c is', c)
print ('d is', d)
print ('e is', e)

