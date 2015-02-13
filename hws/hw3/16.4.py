""" Dallas Hays
    Exercise 16.4
    Homework 3
"""

class Time(object):
    """ Represents the time of day.
        attributes: hour, minute, second
    """

def increment(time, seconds):
    """ Here we increment the seconds in time, and fix the values so they
        remain in bounds.

        Same as 16.3.py except we create a new Time object and give it the
        other times values instead of modifying the original Time object 
    """
    new_time = Time()
    new_time.hour = time.hour
    new_time.minute = time.minute
    new_time.second = time.second + seconds

    if new_time.second >= 60:
        new_time.minute += new_time.second/60
        new_time.second %= 60
    if new_time.minute >= 60:
        new_time.hour += new_time.minute/60
        new_time.minute %= 60
    if new_time.hour > 12:
        new_time.hour %= 12

    print "%.2d:%.2d:%.2d" % (new_time.hour, new_time.minute, new_time.second)

def main():
    t1 = Time()
    t1.hour = 11
    t1.minute = 59
    t1.second = 30
    increment(t1, 3629)
    print "%.2d:%.2d:%.2d" % (t1.hour, t1.minute, t1.second)

main()
