'''
Practical 9, Exercise 2

Ask user for a number
Ensure number is positive
while number is positive
    for all integers in the range of numbers up to and including the chosen number
        add each of these integers
    print the total of these integers
    ask the user to enter a number again

If the number is less than zero, tell the user and stop the program    

'''

num = int (input ('Enter a positive integer: '))
add = 0

while num > 0:
    for i in range (0, num + 1, 1):
        add += i
    print ('The sum of the integers up to', num, 'is', add)
    add = 0
    num = int (input ('Enter a positive integer: '))
    
if num < 0:
    print ('Number is less than zero')
