'''
Practical 9, Exercise 5

Ask user for number of possible toppings
Ask user for numer of toppings on standard pizza
Get the number of the possible toppings minus the number of toppings on a pizza
Tell the user if either number is less than 0
else:
    calculate factorial of all possible toppings
    if toppings is equal to 0, factorial is 1
    else:
        define factn as 1
        for all numbers between 1 and number
        get factn = factn * each number
    if toppings on a standard pizza is equal to 0, factorial is 1
    else:
        define factk as 1
        for all numbers between 1 and number
        get factk = factk * each number

    get the factorial of the difference between the two
    if the difference is equal to 1
        factj is 1
    else:
        define factj as 1
        for all numbers between 1 and number
        get factj = factj * each number

get facti by multiplying factk and factj

Print the possible numbers of combinations which is factn/facti

'''
top = int (input ('Enter the number of possible toppings: '))
top_stand = int (input ('Enter the number of toppings offered on standard pizza: '))

diff = top - top_stand

if top < 0 or top_stand < 0:
    print ('Number entered was less than 0')

else:
    if top == 1:
        factn = 1
    else:
        factn = 1
        for i in range (1, top + 1):
            factn *= i

    if top_stand == 1:
        factk = 1
    else:
        factk = 1
        for j in range (1, top_stand + 1):
            factk *= j

    if diff == 1:
        factj = 1
    else:
        factj = 1
        for k in range (1, diff + 1):
            factj *= k

facti=factk * factj

print ('The number of possible combinations is:', (factn//facti))
