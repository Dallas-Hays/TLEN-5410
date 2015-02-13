""" Dallas Hays
    Exercise 15.1
    Homework 3
"""
import math

class Point(object):
    """ Represents a point in 2-D space."""

def distance_between_points(P1, P2):
    """ Simply does the distance formula using the Point class
        c^2 = a^2 + b^2
    """
    a = (P1.y-P2.y)**2
    b = (P1.x-P2.x)**2
    c = math.sqrt(a+b)
    return c

def main():
    point1 = Point()
    point2 = Point()
    point1.x = 3.0
    point1.y = 4.0
    point2.x = 6.0
    point2.y = 8.0
    print distance_between_points(point1, point2)

main()
