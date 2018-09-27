#Practical 3, exercise 2
#Length taken as 182059.24 - student number
#Area of square = length x height
#Volume of cube = length x length x length
#Area of circle = πr2
#Volume of sphere = 4/3πr3
#Volume of cylinder = πr2h
#π = 3.1415927


length = 182059.24
diameter = 182059.24
radius = (182059.24/2)
height = 182059.24
pi = 3.1415927

area_square = length * length
area_square2 = length**2
print ("The area of a square (l*l) of length 182059.24 is" , area_square)
print ("The area of a square (l2) of length 182059.24 is" , area_square2, "\n")

vol_cube = length * length * length
vol_cube2 = length**3
print ("The volume of a cube (lxlxl) with side 182059.24 is", vol_cube)
print ("The volume of a cube (l3) with side 182059.24 is", vol_cube2, "\n")

area_circle = (pi*radius**2)
print ("The area of a circle with diameter 182059.24 is", area_circle, "\n")

vol_sphere = (4/3*pi*radius**3)
print ("The volume of a sphere with diameter 182059.24 is", vol_sphere, "\n")

vol_cyl = (pi*radius**2*height)
print ("The volume of a cylinder with diameter 182059.24 is", vol_cyl)
