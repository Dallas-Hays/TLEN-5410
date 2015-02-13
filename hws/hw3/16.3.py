""" Dallas Hays
    Exercise 16.3
    Homework 3
"""
class Time(object):
    """ Represents the time of day.
        attributes: hour, minute, second
    """

def increment(time, seconds):
    """ Here we increment the seconds in time, and fix the values so they
        remain in bounds.

        Dividing a time value by 60 will give you how far above 60 the value is
        This is especially useful for large values like 3600
        We also use module for finding the new value of the time value that
        has gone over their limit
    """
    time.second += seconds
    if time.second >= 60:
        time.minute += time.second/60
        time.second %= 60
    if time.minute >= 60:
        time.hour += time.minute/60
        time.minute %= 60
    if time.hour > 12:
        time.hour %= 12

    print "%.2d:%.2d:%.2d" % (time.hour, time.minute, time.second)

def main():
    t1 = Time()
    t1.hour = 11
    t1.minute = 59
    t1.second = 30
    increment(t1, 3629)
    print "%.2d:%.2d:%.2d" % (t1.hour, t1.minute, t1.second)

main()
