#Practical 4, exercise 1
#To ask user to input both amount and exchange rate

amount = int(input('Enter amount to be converted '))

print ('Current amount:', amount)

exchange = int(input('Enter exchange rate '))

print ('The exchange rate chosen is:', exchange)

if amount >= 0:
        print ('Amount after exchange:', amount*exchange)
else:
        print ('Amount must be greater than 0')
        print ('Please try again')

print ('Done!')    
