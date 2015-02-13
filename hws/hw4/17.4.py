""" Dallas Hays
    Exercise 17.4
    Homework 4

    __add__ method allows you to add two Points together
"""

class Point(object):
    """ Represents a point in 2-D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'x=%.2f , y=%.2f' % (self.x, self.y)
    def __add__(self, other):
        new_point_x = self.x + other.x
        new_point_y = self.y + other.y
        new_point = Point(new_point_x, new_point_y)
        return new_point

def main():
    x_val = 15.0
    y_val = 30.0
    mypoint1 = Point(x_val, y_val)
    mypoint2 = Point(25.0, 35.0)
    print mypoint1 + mypoint2

main()
