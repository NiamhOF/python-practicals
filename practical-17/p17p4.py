'''
Practical 17, Exercise 4

Define a function to get a Palindrome:

    nested in this function define a function toChars to make all characters lowercase with only letters
        set the word to lowercase
            assign letterstring no empty value
            for all letters in the string:
                if the letter is in the alphabet:
                    add it to letterstring
            return letterstring

    nested in the Palidrome function is isPal:
        if the length of the word is less than or equal to 1
            the word is a palidrome
        else:
            the word is a palidrome if the first letter is equal to the last and
            the same function is used and all other letters in the string are equal
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
        if len (s) <= 1:
            return True
        
        else:
            return s[0] == s [-1] and isPal (s[1:-1])
        
    return isPal (toChars (s))

str = input ('Enter a string: ')

while str != '':
    
    if isPalindrome (str):
        print (str, 'is a palindrome')
    else:
        print (str, 'is not a palidrome')

    str = input ('Enter a string: ')

print ('Finished')
