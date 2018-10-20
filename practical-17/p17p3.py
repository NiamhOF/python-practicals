'''
Practical 17, Exercise 3

Ask the user to enter a string
make all characters in the string lowercase
if there are no occurances of cat and dog:
    tell the user
else if there is the same amount of words cat as there are of words dog:
    tell user
else:
    print they don't appear the same amount of times.

'''

string = input ('Enter a string: ')
string.lower ()
if string == '':
    print ('Nothing was entered')
elif string.count('cat') == 0 and string.count('dog') == 0:
    print ('There are no occurances of the words cat or dog')
elif string.count('cat') == string.count('dog'):
    print ('The word cat appears the same number of times as the word dog')
else:
    print ('The word cat does not appear the same number of times as the word dog')

