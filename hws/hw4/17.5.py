""" Dallas Hays
    Exercise 17.5
    Homework 4
"""

class Point(object):
    """ Represents a point in 2-D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'x=%.2f , y=%.2f' % (self.x, self.y)

    def __add__(self, other):
        if isinstance(other, Point):
            # Point() + Point()
            return self.add_two_points(other)
        else:
            # Point() + tuple
            return self.add_points_tuple(other)

    def add_two_points(self, other):
        """ Add the attributes of the points, create a new point from them"""
        new_point_x = self.x + other.x
        new_point_y = self.y + other.y
        new_point = Point(new_point_x, new_point_y)
        return new_point

    def add_points_tuple(self, other):
        """ Add the attributes with the values in the tuple: (x,y) """
        new_point_x = self.x + other[0]
        new_point_y = self.y + other[1]
        new_point = Point(new_point_x, new_point_y)
        return new_point

def main():
    x_val = 15.0
    y_val = 30.0
    mypoint1 = Point(x_val, y_val)
    mypoint2 = Point(25.0, 35.0)

    print mypoint1 + mypoint2
    print mypoint1
    print mypoint1 + (39.0, 49.0)

main()
