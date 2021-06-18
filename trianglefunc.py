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

def display_triangle(z):
    import matplotlib.pyplot as plt

    x_values = [z[0], z[2], z[4], z[0]] #add copy of 1st point to end for plotting
    y_values = [z[1], z[3], z[5], z[1]]
    #plt.scatter(x_values, y_values)
    plt.plot(x_values, y_values, 'ro-')
    plt.xlabel('x - axis')
    plt.ylabel('y - axis')
    plt.show()




