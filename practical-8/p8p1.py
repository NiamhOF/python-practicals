'''
Practical 8, Exercise 1

Ask user for a number
Read number
While the number is greater than or equal to 0 perform the following:
    determine if number is divisable by 2, 3, 5 or 7
    if it is, tell the user
    else if it isn't, tell the user
    ask the user for another number
Tell the user if the number is negative

'''

num = int(input ('Enter a number: '))

while num >= 0:
    if num == 0:
        print (num, 'is zero')
    elif num % 2 == 0:
        print (num, 'is divisible by 2')
    elif num % 3 == 0:
        print (num, 'is divisible by 3')
    elif num % 5 == 0:
        print (num, 'is divisible by 5')
    elif num % 7 == 0:
        print (num, 'is divisible by 7')
    else:
        print (num, 'is not divisible by 2, 3, 5 or 7')
    num = int(input ('Enter a number: '))

print ('Number is negative')
