""" Dallas Hays
    Exercise 17.3
    Homework 4

    __str__ method allows you to print a Point()
"""

class Point(object):
    """ Represents a point in 2-D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return 'x=%.2f , y=%.2f' % (self.x, self.y)

def main():
    x_val = 15.0
    y_val = 30.0
    mypoint = Point(x_val, y_val)
    print mypoint
main()
