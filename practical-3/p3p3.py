#Practical 3, exercise 3

Money = 182059.24
Lower_Tax = (Money/100)*13.5/100
Higher_Tax = (Money/100*40)*23/100
Total_Tax = Money + Lower_Tax + Higher_Tax
print ("Total tax amount is", Total_Tax, "\n")

#To ask the user to caluculate tax on amount

gross_tax = int(input('Enter earnings to calculate nett tax: '))
lower_tax = (gross_tax/100*60)*13.5/100
higher_tax = (gross_tax/100*40)*23/100
before_tax = gross_tax + lower_tax + higher_tax

if gross_tax >=0:
    print ('Your total earnings before tax is:', before_tax)
else:
    print ('Amount must be greater than 0')
    print ('Please try again')
