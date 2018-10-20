'''
Practical 19, Exercise 1

Define a function convertBase that takes two parameters number and base:
    assign remainder the value of an empty string
    while the number is greater than 0:
        remainder is equal to remainder + the string (remainder of number divided by base)
        number is equal to number integer divided by base
    return the value of remainder with the string reversed

Ask user for 2 numbers, one the number in base 10 and one the base
if the base is less than 2:
    return an error
else:
    print the result of the function convertBase
'''

def convertBase (number, base):
    '''Function to convert base 10 to another base
        Assumes base is greater than 1'''
    remainder = ''
    while number > 0:
        remainder += str(number % base)
        number //= base
    return remainder [::-1]

number = int (input ('Enter a number in base 10: '))
base = int (input ('Enter a base to convert the number to: '))

if base < 2:
    print ('Base must be greater than 2')

else:
    print (convertBase(number, base))
        
print ('Finished')
