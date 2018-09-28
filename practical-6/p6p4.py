"""
Practical 6, Exercise 4

Create and store a password
Ask the user to enter the password
Count the number of times that password is incorrectly entered
If count equals 3 print "You have been denied access"
If the count is less than 3 and the password has been correctly entered, print "You have successfully logged in"

"""

password = 'abcd'
password_enter = input ("Enter your password: ")
count = 1

if password_enter == password:
    print ("You have successfully logged in.")

else:
    while password_enter != password and count <= 3:
        print ("That is the wrong password")
        password_enter = input ("Enter your password: ")
        count = count + 1
    
    if password_enter == password and count < 3:
        print ("You have successfully logged in.")
    else:
         print ("You have been denied access")


