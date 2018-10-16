'''

Practical 14, Exercise 3

Program to get prime numbers in a range of integers.

For all the numbers in the range 2 to 20 (up to 19), incrementing by 1:
    for i in the range of 1 to the number (inucluding one less than number):
         if the number is divisible by i with no remainder:
             print the multiple that will equal that number
    else:
        if the number does not have a number divisible by anything other than itself
        print that it is a prime number

print finished

'''

for number in range (2, 20):
    for i in range (2, number):
        if number % i == 0:
            print (number, 'equals', i, '*', number//i)
            break
        
    else:
        print (number, 'is a prime number')

print ('Finished!')
