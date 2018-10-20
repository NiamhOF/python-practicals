'''
Practical 18, Exercise 6

import os to check if a file exists
check is p18p6-source.txt and results.txt exist.
if they do not, print an error

Define function stringCount that takes two parameters lines and string
assign count the value 0
for all lines in lines:
    add the number of occurrences of that string to count
return the value of count

Define function lineCount that takes the parameter lines
assign count the value 0
for all lines in lines:
    add one to count
return count

open source file
open output file

define lines as the text from the source file

write the number of < in the source file to the output using the stringCount function
write the number of > in the source file to the output using the stringCount function
write the number of lines in the source file to the output using the lineCount function
write the number of e in the source file to the output using the stringCount function
write the number of <-- in the source file to the output using the stringCount function
write the number of --> in the source file to the output using the stringCount function

close both files

'''
import os

filename = ('p18p6-source.txt')
if not os.path.isfile(filename):
    print ('File ' + filename + ' does not exist')

filename = ('results.txt')
if not os.path.isfile(filename):
    print ('File ' + filename + ' does not exist')

def stringCount(lines, string):
    '''counts occurrances of a string in a line over all lines'''
    count = 0
    for line in lines:
        count = count + line.count(string)
    return count

def lineCount (lines):
    '''counts the number of lines'''
    count = 0
    for line in lines:
        count += 1
    return count

fileHandle = open('p18p6-source.txt', 'r')
results = open ('results.txt', 'w')

lines = fileHandle.readlines()

results.write ('The left angle bracket occurs ' + str(stringCount(lines, '<')) + ' times' + '\n')
results.write ('The right angle bracket occurs ' + str(stringCount(lines, '>')) + ' times' + '\n')
results.write ('There are '+ str(lineCount(lines)) + ' occurrences of newlines' + '\n')
results.write ('There are '+ str(stringCount(lines, 'e')) + ' occurrences of lowercase e characters' + '\n')
results.write ('The string <-- occurs ' + str(stringCount(lines, '<--')) + ' times' + '\n')
results.write ('The string --> occurs ' + str(stringCount(lines, '-->')) + ' times' + '\n')

fileHandle.close()
results.close()
