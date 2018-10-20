'''
Practical 19, Exercise 2

Define a function convertToInteger that takes a parameter digit:
    if that parameter is in 0 - 9:
        return the number as an integer
    elif make digit lwercase and if a - f assign values 10 - 15 respectively

Define a function convertBaseten that takes the parameter number and base:
    Assign baseTen and power the value 0
    reverse the order of characters in number and assign this to digits
    for all values in digits:
        Assign intDigit the value after passing it through the function convertToInteger
        Assign baseTen the value baseTen + intDigit x parameter base to the power of its position in the reversed number
        Add one to power
    return baseTen

Ask user for a number to cenvert to base ten and the base which it is converting from
for all values in number:
    if it is not abcdefABCDEF1234567890
        print an error
        break to stop it running once an error is found
    else:
        pass the parameters through the function convertBaseten and print the result
        break
'''
def convertToInteger(digit):
    '''Function to give values to a - f, whether upper or lower case'''
    if digit in '0123456789':
        return int(digit)
    elif digit.lower() == 'a':
        return 10
    elif digit.lower() == 'b':
        return 11
    elif digit.lower() == 'c':
        return 12
    elif digit.lower() == 'd':
        return 13
    elif digit.lower() == 'e':
        return 14
    elif digit.lower() == 'f':
        return 15
    
def convertBaseten (number, base):
    '''Function to convert a number from another base to base 10'''
    baseTen = 0
    power = 0
    digits = str(number)[::-1]
    for digit in digits:
        intDigit = convertToInteger(digit)
        baseTen += intDigit * base ** power
        power += 1
    return baseTen

number = input ('Enter a number to convert to base 10: ')
base = int (input ('Enter the base number to convert from: '))

for digit in number:
    if digit not in 'abcdefABCDEF1234567890':
        print ('Number must be in 0 - 9 and A - F')
        break
    else:
        print (number, 'with base', base, 'converted to base 10 is', convertBaseten(number, base))
        break

