"""
Practical 7, Exercise 4

Add all numbers from 1 - 5000
Add 1 to 2 to 3 etc. up to 5000
Add first 2 numbers - take the sum of that and add it to the next number
Print out total.

"""

number = 1
total = 0

while number <= 5000:
    total = total + number
    number = number + 1
    
print (total)
