"""
Practical 7, Exercise 5

Get the range of numbers from 1 to 10000 in increments of 1
Determine all numbers divisibile by 3
Determine all numbers divisible by 5
Sum all of these numbers
Print the total

"""
total = 0

for i in range (1, 10001):
    if i % 3 == 0 or i % 5 == 0:
        total += i
print (total)
