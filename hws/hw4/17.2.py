""" Dallas Hays
    Exercise 17.2
    Homework 4
2,3,4,5,7

    __init__ allows you to set variables of Point as arguments
"""

class Point(object):
    """ Represents a point in 2-D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

def main():
    x_val = 15.0
    y_val = 30.0
    mypoint = Point(x_val, y_val)
    print mypoint.x, mypoint.y
main()
