'''
Practical 18, Exercise 3

Define a function isLetter
    checks that character is a lowercase letter

Define a function isCode
    assign numcode the value 0
    if the length of the string is less than 4 characters
        return an error
    else:
        for all characters in the range 0 to the length of the string:
            if the first letter is c and second is 0 and the third is a letter and the fourth is an e:
                add one to numcode
        return numcode

Ask user for a string
print the function isCode

'''
def isLetter(s):
    '''check that character is a letter'''
    return s.lower() in 'abcdefghijklmnopqrstuvwxyz'

def isCode (s):
    '''takes string and counts how many times the word code is in it'''
    numcode = 0
    if len (s) < 4:
        print ('Error. Word must be longer than 3 letters.')
    else:
        for i in range (0, len(s) - 3):
            if s [i] == 'c' and s [i + 1] == 'o' and isLetter(s[i + 2]) and s[i + 3] == 'e':
                numcode += 1
    return numcode

word = input ('Enter a string: ')

print (isCode(word))
