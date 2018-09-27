#Practical 4.5, exercise 2

import math

length = int(input('Enter length '))
radius = length/2
area_square = length**2
vol_cube = length**3
area_circle = math.pi*length**2
vol_sphere = (4/3*math.pi*length**3)
vol_cyl = (math.pi*length**2*length)

if length >= 0:
    print ('\nThe area of a square with side length of', length, 'is', area_square)
    print ()
    print ('The volume of a cube with side length of', length, 'is', vol_cube)
    print ()
    print ('The area of a circle with radius of length', length, 'is', area_circle)
    print ()
    print ('The volume of a sphere with radius of length', length, 'is', vol_sphere)
    print ()
    print ('The volume of a cylinder with radius of length', length, 'and side of length', length, 'is', vol_cyl)
else:
    print ('Length must be >= 0. Please try again')

#Error if, if statement has a capital letter - Invalid syntax
#Error if the if or else statement does not include the : - Invalid syntax
#If all of the above are indented - error of unexpected indent - does not run
