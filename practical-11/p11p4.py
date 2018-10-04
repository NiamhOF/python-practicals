'''

Practical 11, Exercise 4

Get the factorial of 2n
get the factorial of n+1
get the factorial of n
multiply factorial of n+1 and n
use this to divide the factorial of 2n by
print the series

'''
number = int (input ('Enter a number to get the Catalan Numbers: '))

if number < 0:
    print ('Number must be greater than zero')

else:
        
    if number == 0:
        print ('Catalan Number is 1')
        
    else:
        print ('Series is: 1', sep = '', end = "")

        fact2n = 1
        factn1 = 1
        factn = 1
        count = 1
                
        for i in range (1, (number*2) + 1):
            fact2n *= i

        for j in range (1, (number +1 ) +1):
            factn1 *= j

        for k in range (1, number + 1):
            factn *= k

        facteq = fact2n//(factn1 * factn)

        count = 1
        while count <= number:
            for l in range (1, number +1):
                fact = count * facteq
                print (',', fact, end ="")
                count += 1
            
                
