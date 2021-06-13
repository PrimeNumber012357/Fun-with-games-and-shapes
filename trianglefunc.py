import math

def main():
    c = ["first", "second", "third"]
    i = 0
    points = []
    while i < 3:
        try:
            x, y = input("Enter a value for x and y separated by a space for your {} point: ".format(c[i])).split()
            float(x)
            float(y)
            i += 1
            points.append(float(x))
            points.append(float(y))
        except ValueError:
            print("You didn't enter 2 numbers.  Try again")
    if validate_triangle(points):
        print("The perimeter of your triangle is...{}".format(distance(points)))
    else:
        print("Not a valid triangle")

def distance(z):
    d1 = math.sqrt(((z[2] - z[4])**2 + (z[3] - z[5])**2))
    d2 = math.sqrt(((z[0] - z[2])**2 + (z[1] - z[3])**2))
    d3 = math.sqrt(((z[4] - z[0])**2 + (z[5] - z[1])**2))
    sum = d1 + d2 + d3
    return sum


def get_area(z):
    return abs(0.5*(z[0]*(z[3]-z[5])) + (z[2]*(z[5]-z[1])) + (z[4]*(z[1]-z[3])))

#If the area is zero the points have not created a triangle
def validate_triangle(z):
    if len(z) == 6:
        area = get_area(z)
        if area == 0:
            return False
        else:
            return True
    else:
        return False

#Can't figure out how to get matplotlib to connect all the points
def display_triangle(z):
    import matplotlib.pyplot as plt

    x_values = [z[0], z[2], z[4]]
    y_values = [z[1], z[3], z[5]]
    point_1 = [x_values[0], y_values[0]]
    point_2 = [x_values[1], y_values[1]]
    point_3 = [x_values[2], y_values[2]]
    #plt.plot(point_1,point_3, 'ro-')
    #plt.plot(point_3,point_1, 'ro-')
    #plt.plot(point_1,point_2, 'ro-')
    plt.scatter(x_values, y_values)
    #plt.plot(x_values, y_values)
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.show()
    print(point_1)



