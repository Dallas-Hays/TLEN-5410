""" Dallas Hays
    Exercise 16.1
    Homework 3
"""
class Time(object):
    """ Represents the time of day.
        attributes: hour, minute, second
    """

def print_time(time):
    print "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)

def main():
    new_time = Time()
    new_time.hour = 11
    new_time.minute = 59
    new_time.second = 30
    print_time(new_time)
main()
