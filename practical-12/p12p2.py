'''

Practical 12, Exercise 2

(a) define a function for the fibonacci sequence taking a number:
        define f_0 as 1
        define f_1 as 1
        if the number is 0:
            print f_0
        elif the number is 2:
            print the series of f_0 and f_1
        else:
            print the series of f_0 and f_1 with no seperation and no new line
            define a and b as f_0 and f_1
            for all numbers in the range i from 2 up to the number:
                define fibon as a plus b
                print each of these vaules with no new line
                after each number has been printed
                define a and b as b and fibon respectively
                
(b) Ask user for a number
    if the number is 0 or less:
        print an error
    else:
        use the function above

'''

def fib(num):
    f_0 = 0
    f_1 = 1
    if num == 1:
        print ('Series is: ', f_0)
    elif num == 2:
        print ('Series is: ', f_0, ', ', f_1, sep = "")
    else:
        print ('Series is: ', f_0, ', ', f_1, sep = "", end = "")
        a, b = f_0, f_1
        for i in range (2, num):
            fibon = a + b
            print (',', fibon, end = "")
            a, b = b, fibon

number = int (input ('Enter a number to get the Fibonacci Series: '))

if number <= 0:
    print ('Error. Number must be greater than zero')
else:
    fib(number)
