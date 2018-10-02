'''

Practical 8, Exercise 2

Ask user for a number
Read number
Define i as 1
while i is less than or equal to number
    j = 1
        while j is less than or equal to number
            print j * i and a space. Ensure new line is not started
            add 1 to j
    add 1 to i
    print a new line

'''

table_size = int(input ('Enter a number to get the multiplication table: '))
i = 1

while i <= table_size:
    j = 1
    while j <= table_size:
        print (j * i, '\t', end = '')
        j += 1
    i += 1
    print ()
