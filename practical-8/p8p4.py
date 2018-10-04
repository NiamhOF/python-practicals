'''

Practical 8, Exercise 4

Ask user for a number
Set a count value of 0 for each condition
while the number is greater than or equal to 0 continue the loop
    if number = 0, tell user and count input
    if number > 0 and less than or equal to 20, tell user and count
    if number > 20 and less than or equal to 40, tell user and count
    if number > 40 and less than or equal to 60, tell user and count
    if number > 60 and less than or equal to 80, tell user and count
    if number > 80 and less than or equal to 100, tell user and count
    if number is greater than 100, tell user and count
if the number is negative, tell user
Tell user how many times each condition was entered

'''

num = int (input ('Enter a number: '))
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0

while num >= 0:
    if num == 0:
        print ('Number is equal to 0')
        count1 += 1
    elif 0 < num <= 20:
        print ('Number is greater than 0 and less than or equal to 20')
        count2 += 1
    elif 20 < num <= 40:
        print ('Number is greater than 20 and less than or equal to 40')
        count3 += 1
    elif 40 < num <= 60:
        print ('Number is greater than 40 and less than or equal to 60')
        count4 += 1
    elif 60 < num <= 80:
        print ('Number is greater than 60 and less than or equal to 80')
        count5 += 1
    elif 80 < num <= 100:
        print ('Number is greater than 80 and less than or equal to 100')
        count6 += 1
    elif num > 100:
        print ('Number is greater than 100')
        count7 += 1
    num = int (input ('Enter a number: '))

if num < 0:
    print ('Number is less than 0')
    print ('You have entered the number 0', count1, 'times')
    print ('You entered a number greater than 0 and less than or equal to 20', count2, 'times')
    print ('You entered a number greater than 20 and less than or equal to 40', count3, 'times')
    print ('You entered a number greater than 40 and less than or equal to 60', count4, 'times')
    print ('You entered a number greater than 60 and less than or equal to 80', count5, 'times')
    print ('You entered a number greater than 80 and less than or equal to 100', count6, 'times')
    print ('You entered a number greater than 100', count7, 'times')

    
