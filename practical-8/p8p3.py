'''

Practical 8, Exercise 3

Ask user for a number
Set count at 1
while the count is less than or equal to 20
    for all numbers between and including 0 and 20
        print each number and each number multiplied by the users number
        add 1 to count

'''

num = int (input ('Enter a number: '))
count = 1

while count <= 20:
    for i in range (0, 21, 1):
        print (i, ' ', i * num)
        count += 1
        
