'''

Practical 14, Exercise 5

Use recusrion to show fibonacci sequence

(a) Define a function fibon (n):
        if n is less than or equal to 1:
            return n (state in program to be 0 or positive)
        else:
            return fibon(n-1) + fibon (n-2) - recursion

(b) Ask user to input a number
while number is greater than or equal to 0:
    print Fibonacci sequence with no new line
    for all values of i in the range up to the number:
        print (the return of the function fibon with a comma and no new line)

if the number is less than zero:
    print an error

(c) Print statements added to function to show workings. Uncomment to see
print number being evaluated
print (n-1) + (n-2) of that number
print fibon (n-1) + (n -2)

'''

def fibon(n):    
    """Recursive function to print the Fibonacci sequence"""
    if n <= 1:
        return n
    
    else:
        
        '''Print statements used to show the recursion working. Uncomment to see'''
        '''
        print ()
        print ('Number being evaluated is: ', n)
        print ('Working out the Fibonacci using (n-1) + (n-2): ', (n-1)+(n-2))
        print ('Working out the Fibonacci using fibon(n-1) + fibon(n-2): ', fibon(n-1)+fibon(n-2))
        print ()
        '''
        return fibon(n-1) + fibon(n-2)

number = int (input ('Enter a number to get the Fibonacci sequence: '))

while number >= 0:
    print ("Fibonacci sequence is: ")
    for i in range(number):
        print (fibon(i))
    print ()
    number = int (input ('Enter a number to get the Fibonacci sequence: '))
 
if number < 0:
   print ('Number must not be less than 0')
