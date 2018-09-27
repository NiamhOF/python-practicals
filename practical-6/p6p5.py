"""
Practical 6, Exercise 5

Create and store a password
Ask user to enter a password
If the password is correct, print "You have successfully logged in"
If password is wrong, print "Sorry, the password is wrong" and ask user to re-enter password three times
If the password is correct three times, print "You have successfully logged in"
If not correct any of the three time, print "You have been denied access"

"""

password = '1234'
password_enter = input("Enter your password: ")
count = 1

if password_enter == password:
    print ("You have successfully logged in.")

elif password_enter != password:
    print ("Sorry the password is wrong")

    password_enter = input ("Enter the correct password three times to verify: ")

    while password_enter == password and count < 3:
        password_enter = input ("Enter the correct password three times to verify: ")
        count = count + 1

    if password_enter != password:
         print ("You have been denied access")
    else:
        password_enter == password and count == 3
        print ("You have successfully logged in")


