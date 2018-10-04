'''

Practical 11, Exercise 1

Ask user to input a number to calculate the factorial
if number less than 0:
    tell user. Finish program

else:
    define fact as 1
    for i in the range of numbers up to and including number
        fact is fact times i
    print the factorial and finish

'''

number = int (input ('Enter a number to calculate the factorial: '))

if number < 0:
    print ('Error. Number is less than 0.')
    
else:
    fact = 1
    for i in range (1, number +1):
        fact *= i
        
    print ('Factorial of', number, 'is', fact)
