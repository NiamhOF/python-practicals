'''

Practical 10, Exercise 3

ask user for a string
while that string is not empty:
    define count as 0
    for each letter in the string
        if aeiou is in it
            count is defined as count plus 1
    print the number of vowels
    ask user for another input
if an empty string tell user and exit

'''

string = input ('Enter a word or words: ')

while string !="":
    count = 0
    for letter in string:
        if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u' or letter == 'A' or letter == 'E' or letter == 'I' or letter == 'O' or letter == 'U':
            count += 1
    print (string, 'has', count, 'vowels in it')
    string = input ('Enter a word or words: ')

print ('Nothing entered. Program finished')
