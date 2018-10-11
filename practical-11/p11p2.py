'''
Practical 11, Exercise 2

Ask user for a number
if number equal to or less than zero:
    print error
else if number is 1:
    print that the series is 0
else if number is 2:
    print the series is 0 and 1
else:
    print the series is 0 and 1 - ensure ot does not go to a new line
    assign a and b to 0 and 1 respectively
    assign i the value 2
    while i is less than the number
        fib has the value a plus b
        print fib - ensure no new line
        assign a and b the values b and fib respectively
        give i the value i + 1


'''

number = int (input ('Enter a number: '))

if number <= 0 :
    print ('Error: number of terms less than or equal 0')

elif number == 1:
    print ('Series is: ', 0)

elif number == 2:
    print ('Series is: ', 0, ', ', 1, sep = "")

else:
    print ('Series is: ', 0, ', ', 1, sep = "", end = "")

    a, b = 0, 1
    i = 2
    while i < number:
           fib = b + a
           print (',', fib, end = "")

           a, b = b, fib
           i += 1
