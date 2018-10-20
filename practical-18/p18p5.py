'''
Practical 18, Exercise 5
Define a function isXyz that takes the parameter s:
    if the no. of occurances of xyz is not equal to the no. of occurances of .xyz
        return True
    else:
        return False

Ask user to input a string

print the function isXyz with the parameter as the string

'''
def isXyz (s):
    '''counts no. of occurance of xyz and .xyz'''
    if s.count ('xyz') != s.count ('.xyz'):
        return True
    else:
        return False

string = input ('Enter a string: ')

print (isXyz(string))
