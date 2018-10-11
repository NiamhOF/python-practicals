'''

Practical 11, Exercise 4

Ask user for a number
if the number is less than zero
    print an error
else: 
    print that if number is 0, the Catalan Series is 1
    define cn as 1
    for all numbers from 0 up to the number:
        define numerator as 2 times by ( 2 by n +1)
        define denominator as n + 2
        define catalan as an integer of numerator divided by denominator multiplied by cn
        define cn as catalan
        print the series
    
'''
number = int (input ('Enter a number to get the Catalan Numbers: '))

if number < 0:
    print ('Number must be greater than zero')

else:
    print ('Catalan series of ', number, ' is: ', '1', sep = '', end = '')      
    cn = 1
    for n in range (0, number):
        numerator = 2 * (2 * n + 1)
        denominator = n + 2

        catalan = int((numerator/denominator) * cn)
        cn = catalan

        print (", ", catalan, end = "")
