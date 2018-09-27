#Practical 4.5, exercise 1
#To ask user to input both amount and exchange rate.
#Include if statement

amount = int(input('Enter amount to be converted '))

print ('Current amount:', amount)

exchange = int(input('Enter exchange rate '))

print ('The exchange rate chosen is:', exchange)

if amount >= 0 and exchange >=0:
        print ('Amount after exchange:', amount*exchange)

#If the if statement is indented or either print command above this - idle detects an unexpected indent and won't run
#If print amount after exchange is not indented - idle detects that it should be indented and won't run

else:
    print ('Amount and exchange rate must be greater than 0')
    print ('Please try again')
    
#If else only is indented - idle detects a syntax error
#If else and print are both indented further - invalid syntax is detected
#If print under else is further indented - code will run
