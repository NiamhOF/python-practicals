#Practical 5, Exercise 4

number = int(input('Enter a number: '))

if number == 0:
    print ('Number is equal to 0')

elif 0 < number and number <= 20:
    print ('Number is greater than 0 and less than or equal to 20')

elif 20 < number and number <= 40:
    print ('Number is greater than 20 and less than or equal to 40')

elif 40 < number and number <= 60:
    print ('Number is greater than 40 and less than or equal to 60')

elif 60 < number and number <= 80:
    print ('Number is greater than 60 and less than or equal to 80')

elif 80 < number and number <= 100:
    print ('Number is greater than 80 and less than or equal to 100')

elif number > 100:
    print ('Number is greater than 100')

else:
    print ('Number is less than 0')
