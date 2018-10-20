'''
Practical 18, Exercise 5 alternate

Define a function hasNoPrefix that takes two parameters index and s:
    if index is equal to zero return true
    else if the index position - 1 is a period return False
    else:
        return True

Define a function is XYZ that takes the parameter s:
    assign containsXYZ the value false
    if the length of the string is greater than 2:
        for all values of i in the range 0 to length of string -2:
            if the first position of i is x and the second position of i is y and the third position of i is z:
                if passing i and the string through hasNoPrefix is true:
                    containsXYZ is assigned the value true
                    break once this has been shown to be true
    return containsXYZ if the above is not true

Ask user to input a string

print the function isXYZ with the parameter word

'''
def hasNoPrefix(index, s):
    '''takes an index and a string and checks for a period'''
    if index == 0:
        return True
    elif s[index - 1] == '.':
        return False
    else:
        return True

def isXYZ (s):
    '''takes string and checks if xyz is in it'''
    containsXYZ = False
    if len (s) > 2:
        for i in range (0, len(s) - 2):
            if s [i] == 'x' and s [i + 1] == 'y' and s[i + 2] == 'z':
                if hasNoPrefix(i, s):
                    containsXYZ = True
                    break
    return containsXYZ

word = input ('Enter a string: ')

print (isXYZ(word))
