'''

Practical 11, Exercise 3

Ask user for a number
while number is greater than 0:
    if number equals 1:
        tell user the series is 0
    else if number equals 2:
        tell user the series is 0, 1
    else:
        print the series is 0, 1 - ensure no new line
        assign a and b the values 0 and 1 respectively
        for all numbers in the range up to the number:
            assign a as b and b as a + b
            print b - ensure no new line
    print a new line

if number < 0 tell user and finish program

'''

number = int (input ('Enter a number: '))

while number > 0:

    if number == 1:
        print ('Series is: ', 0)

    elif number == 2:
        print ('Series is: ', 0, ', ', 1, sep = "")

    else:
        print ('Series is: ', 0, ', ', 1, sep = "", end = "")
        a, b = 0, 1
        for i in range (2, number):
            a, b = b, a + b

            print (',', b, end ='')
            
    print ()
            
    number = int (input ('Enter a number: '))

print ('Number is zero or less. Program finished')
