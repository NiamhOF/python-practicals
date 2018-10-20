'''
Practical 18, Exercise 2

Define a function isCode
    assign numcode the value 0
    if the length of the string is less than 4
        print an error
    for all characters in the range 1 to the length of the string:
        starting from the first letter in the string check if the next 4 letter are code
            add 1 to numcode to move the position in the string on
    return numcode

Ask user for a string
print the function isCode

'''

def isCode (s):
    '''takes string and counts how many times the word code is in it'''
    numcode = 0
    if len(s) < 4:
        print ('Error. Word must be longer than 3 letters.')
    else:
        for i in range (1, len(s)):
            if s [i -1: i + 3] == 'code':
                numcode += 1
    return numcode

word = input ('Enter a string: ')

print (isCode(word))
