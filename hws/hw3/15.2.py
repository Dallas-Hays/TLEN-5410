""" Dallas Hays
    Exercise 15.2
    Homework 3
"""
class Point(object):
    """ Represents a point in 2-D space."""

class Rectangle(object):
    """ Represents a rectangle.
        attributes: width, height, corner.
    """
def move_rectangle(rect, dx, dy):
    """ Moves a rectangle by adding the values of dx and dy to
        the rectangles corner values.
    """
    rect.corner.x += dx
    rect.corner.y += dy

def main():
    rect = Rectangle()
    rect.width = 100.0
    rect.height = 200.0
    rect.corner = Point()
    rect.corner.x = 300.0
    rect.corner.y = 400.0
    move_rectangle(rect, 150.0, 250.0)
    print rect.corner.x

main()
