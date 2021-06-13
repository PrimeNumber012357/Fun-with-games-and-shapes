#This file is for calling and testing methods from trianglefunc.py

import trianglefunc
#z is the list of all desired point values [x1 y1 x2 y2 x3 y3]
z = [0, 0, 1, 1, 2, 5]

#trianglefunc.main()

#Checking to see if the points create a triangle and return perimeter and area
if trianglefunc.validate_triangle(z):
    print("This triangle is valid and its perimeter is...{:.2f}".format(trianglefunc.distance(z)))
    print("Its area is...{:.2f}".format(trianglefunc.get_area(z)))
else:
    print("Not a valid triangle")

#Can't get matplotlib to connect all the points
trianglefunc.display_triangle(z)
