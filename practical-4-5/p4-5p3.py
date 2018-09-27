# Practical 4.5, exercise 3

income = int(input('Enter income to calculate tax: '))
lower_tax = (income/100*60)*23/100
higher_tax = (income/100*40)*41/100
total_tax = lower_tax + higher_tax
total_nett = income - total_tax

if income >= 0:
    print ()
    print ('Your income is:', income)
    print ()
    print ('Your tax at 23% is:', lower_tax)
    print ()
    print ('Your tax at 41% is:', higher_tax)
    print ()
    print ('Your total tax is:', total_tax)
    print ()
    print ('Your nett income is:', total_nett)

else:
    print ()
    print ('Amount of income must be >= 0. Please try again')
    
#Error if, if statement has a capital letter - Invalid syntax
#Error if the if or else statement does not include the : - Invalid syntax
#If all of the above are indented - error of unexpected indent - does not run
