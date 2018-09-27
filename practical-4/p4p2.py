#Practical 4, exercise 2

import math

length = int(input('Enter length '))
radius = length/2
area_square = length**2
vol_cube = length**3
area_circle = math.pi*length**2
vol_sphere = (4/3*math.pi*length**3)
vol_cyl = (math.pi*length**2*length)

print ('\nThe area of a square with side length of', length, 'is', area_square)
print ('The volume of a cube with side length of', length, 'is', vol_cube)
print ('The area of a circle with radius of length', length, 'is', area_circle)
print ('The volume of a sphere with radius of length', length, 'is', vol_sphere)
print ('The volume of a cylinder with radius of length', length, 'and side of length', length, 'is', vol_cyl)
