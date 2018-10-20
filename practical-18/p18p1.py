'''
Practical 18, Exercise 1

Define a function to get a Palindrome:

    nested in this function define a function toChars to make all characters lowercase with only letters
        set the word to lowercase
            assign letterstring no empty value
            for all letters in the string:
                if the letter is in the alphabet:
                    add it to letterstring
            return letterstring

    nested in the Palidrome function is isPal:
        assign i the value 0
        if the length of the word is less than or equal to 1
            the word is a palidrome
        else:
            while the value of i is less than half the length of the word + 1
                if the first letter in the string is equal to the last letter in the string
                take the value of i away from -1 to keep moving through the right hand side letters.
                    add 1 to i
    return the function isPal passing toChars through it

Ask user for a string
While the string is not empty:
    if the palindrome function of the string is true:
        print that it's a palindrome
    else:
        print it is not a palindrome

    ask user to put in another string

print finished
'''

def isPalindrome (s):
    '''Function to get a palindrome'''
    
    def toChars (s):
        '''Function to convert all characters to lowercase with only letters'''
        s = s.lower()
        letterstring = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                letterstring += c
        return letterstring

    def isPal (s):
        '''Checks if word is a palindrome'''
        i = 0
        if len (s) <= 1:
            return True
        else:
            while i < len(s)/2 + 1:
                if s[i] == s[-1 -i]:
                    i += 1
                    return True
                return False
        
    return isPal (toChars (s))

str = input ('Enter a string: ')

while str != '':
    
    if isPalindrome (str):
        print (str, 'is a palindrome')
    else:
        print (str, 'is not a palidrome')

    str = input ('Enter a string: ')

print ('Finished')
