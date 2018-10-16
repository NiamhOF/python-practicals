'''
Practical 15, Exercise 2

Program using recursion to get f(n) = f(n-1) + 2 to the power of (n-1)

(a) Define function fun(n)
    if n is less than or equal to 1
        return 1
    else:
    return (n-1) + 2**(n-1)

(b) Ask user for a number
    while number is greater than or equal to 1:
        for all values in the range i up to number
            print the function fun of that number
        ask the user for another number

    if the number is less than 1:
        print an error

(c) print statement added to function to show the number being evaluated
    print statement added to function to show (n-1) + 2**(n-1)
    uncomment to see

'''

def fun(n):
    """Recursive function to get (n-1) + 2**(n-1)"""
    if n <= 1:
        return 1
    else:
        
        #Print statements used to show the recursion working. Uncomment to see
        '''
        print ()
        print ('Number being evaluated is: ', n)
        print ('Working out using fun(n-1) + 2**(n-1): ', fun(n-1) + 2**(n-1))
        print ()
        '''
        return (fun(n-1) + 2**(n-1))

number = int (input ('Enter a number: '))

while number >= 1:
    for i in range (number + 1):
        print (fun(i))
    print ()
    number = int (input ('Enter a number: '))

if number < 1:
    print ('Error. Number must be greater than or equal to 1')
