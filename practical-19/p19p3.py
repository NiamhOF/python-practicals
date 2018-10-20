'''
Practical 19, Exercise 3

Import os to check if files exist

Define function stringCount that takes two parameters lines and string
assign count the value 0
for all lines in lines:
    add the number of occurrences of that string to count
return the value of count

ask user to input a filename
check if file exists
print an error if it doesn't

open the file entered
define lines as the text from the source file

count all <, >, (, ), {, }, [, ] and print the amount of each

check if there is an equal amount of each type of bracket
print if there is
print if there is not

'''

import os

def stringCount(lines, string):
    '''counts occurrances of a string in a line over all lines'''
    count = 0
    for line in lines:
        count = count + line.count(string)
    return count

filename = input ('Enter a file name: ')

file = (filename)
if not os.path.isfile(filename):
    print ('File ' + file + ' does not exist')

fileHandle = open(filename, 'r')

lines = fileHandle.readlines()

leftAngle = str(stringCount(lines, '<'))
rightAngle = str(stringCount(lines, '>'))
leftPar = str(stringCount(lines, '('))
rightPar = str(stringCount(lines, ')'))
leftCurl = str(stringCount(lines, '{'))
rightCurl = str(stringCount(lines, '}'))
leftSquare = str(stringCount(lines, '['))
rightSquare = str(stringCount(lines, ']'))

print ('The left angle bracket occurs', leftAngle, 'times')
print ('The right angle bracket occurs', rightAngle, 'times')
print ('The left parenthesis bracket occurs', leftPar, 'times')
print ('The right parenthesis bracket occurs', rightPar, 'times')
print ('The left curly bracket occurs', leftCurl, 'times')
print ('The right curly bracket occurs', rightCurl, 'times')
print ('The left square bracket occurs', leftSquare, 'times')
print ('The right square bracket occurs', rightSquare, 'times')

if leftAngle == rightAngle:
    print ('There is an equal number of angle brackets')
else:
    print ('There is not an equal number of angle brackets')
if leftPar == rightPar:
    print ('There is an equal number of parentheses')
else:
    print ('There is not an equal number of parentheses')
if leftCurl == rightCurl:
    print ('There is an equal number of curly brackets')
else:
    print ('There is not an equal number of curly brackets')
if leftSquare == rightSquare:
    print ('There is an equal number of square brackets')
else:
    print ('There is not an equal number of square brackets')

fileHandle.close()
