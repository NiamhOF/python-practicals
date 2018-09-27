"""
Practical 6, Exercise 3

Ask user for a name
If user inputs Niamh O'Flaherty, print 'That is a cool name!'
Else if user inputs Mickey Mouse, print 'I am not sure that is your name.'
Else if user inputs Spongebob Squarepants, print 'I am not sure that is your name.'
Else if none of these is the input, print 'You have a nice name'

"""

name = input ("What is your name? ")

if name == "Niamh O'Flaherty":
    print ("That is a cool name!")
elif name == "Mickey Mouse":
    print ("I am not sure that is your name.")
elif name == "Spongebob Squarepants":
    print ("I am not sure that is your name.")
else:
    print ("You have a nice name")
