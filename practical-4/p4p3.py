#Practical 4, exercise 3

gross_tax = int(input('Enter earnings to calculate nett tax: '))
lower_tax = (gross_tax/100*60)*13.5/100
higher_tax = (gross_tax/100*40)*23/100
before_tax = gross_tax + lower_tax + higher_tax

if gross_tax >=0:
    print ('\nYour gross tax is:', gross_tax)
    print ('Your tax at 13.5% is:', lower_tax)
    print ('Your tax at 23% is:', higher_tax)
    print ('The total tax you pay is:', lower_tax + higher_tax)
    print ('Your total earnings before tax is:', before_tax)
else:
    print ('Amount must be greater than 0')
    print ('Please try again')
