'''
Practical 9, Exercise 1

Ask user for a number
Tell user is number is less than 0
Define i and addition of i as 0
while i is less than or equal to number
    add = add + 1
    increase i by 1
print the sum of the integers

'''

num = int (input ('Enter a positive number: '))

if num < 0:
    print ('Number is less than zero')

i = 0
add = 0

while i <= num:
    add += i
    i += 1
print ('The sum of the integers up to', num, 'is', add)
