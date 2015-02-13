""" Dallas Hays
    Exercise 16.2
    Homework 3
"""

class Time(object):
    """ Represents the time of day.
        attributes: hour, minute, second
    """

def is_after(t1, t2):
    """ Returns true if t2 comes chronologically before t1
        Uses lists because it allows me to do it without an if statement
    """
    l1 = [t1.hour, t1.minute, t1.second]
    l2 = [t2.hour, t2.minute, t2.second]
    return l1 > l2

def main():
    t1 = Time()
    t2 = Time()
    t1.hour = 11
    t1.minute = 12
    t1.second =  13
    t2.hour = 10
    t2.minute = 59
    t2.second = 0
    print is_after(t1,t2)

main()
