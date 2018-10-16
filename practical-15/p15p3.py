'''
Practical 15, Exercise 3

Program using recursion to get f(n) = f(n-2) + 13 x f(n-1)

(a) Define function fun(n)
    if n is greater than or equal to 0:
        if n equals 0:
            return 13
        else if n equals 1:
            return 8
        else:
            return fun (n-2) + (13 * fun (n-1))

(b) Ask user for a number
    while number is greater than or equal to 0:
        for all values in the range i up to number
            print the function fun of that number
        ask the user for another number

    if the number is less than 0:
        print an error

(c) print statement added to function to show the number being evaluated
    print statement added to function to show fun(n-2) + 13 * fun(n-1)
    uncomment to see

'''

def fun(n):
    
    """Recursive function to get fun(n-2) + 13 x fun(n-1)""" 
   
    if n == 0:
        return 13
    elif n == 1:
        return 8
    else:
        
        #Print statements used to show the recursion working. Uncomment to see
        '''
        print ()
        print ('Number being evaluated is: ', n)
        print ('Working out using fun(n-2) + 13 * fun(n-1): ', fun(n-2) + 13 * fun(n-1))
        print ()
        '''
    return fun(n-2) + (13 * fun(n-1))

number = int (input ('Enter a number: '))

while number >= 0:
    for i in range (0, number + 1):
        print (fun(i))
    print ()
    number = int (input ('Enter a number: '))

if number < 0:
    print ('Error. Number must be greater than or equal to 0')
