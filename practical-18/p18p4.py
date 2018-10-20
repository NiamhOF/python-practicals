'''
Practical 18, exercise 4

Define the function isWord that takes two parameters w1 and w2
    Make both parameters lower case using the lower methog
    using the endswith method if w1 ends with w2 or w2 ends with w1:
        return True
    otherwise return False
    
Ask the user for two inputs

print the function isWord passing the two words in as parameters

'''

def isWord(w1, w2):
    '''check if either of the strings appears at the end of the other'''
    w1 = w1.lower()
    w2 = w2.lower()
    if w1.endswith(w2) or w2.endswith(w1):
        return True
    return False


word1 = input ('Enter a string: ')
word2 = input ('Enter another string: ')

print (isWord (word1, word2))
