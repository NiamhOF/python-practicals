'''
Practical 15, Exercise 1

Program using recursion to get f(n) = n + f(n-1)

(a) Define function fun()
    if n is equal to 1
        return 2
    else:
    return n + fun (n - 1)

(b) Ask user for a number
    while number is greater than or equal to 1:
        for all values in the range i from 1 up to number
            print the function fun of that number
        ask the user for another number

    if the number is less than 1:
        print an error

(c) print statement added to function to show the number being evaluated
    print statement added to function to show n + fun (n -1)
    uncomment to see

'''

def fun(n):
    
    """Recursive function to get n + f(n-1)"""
    
    if n <= 1:
        return 2
    else:
        
        '''Print statements used to show the recursion working. Uncomment to see'''
        '''
        print ()
        print ('Number being evaluated is: ', n)
        print ('Working out using n + fun(n-1): ', n + fun(n-1))
        print ()
        '''
        return (n + fun(n-1))

number = int (input ('Enter a number: '))

while number >= 1:
    for i in range (1, number + 1):
        print (fun(i))
    print ()
    number = int (input ('Enter a number: '))

if number < 1:
    print ('Error. Number must be greater than or equal to 1')
