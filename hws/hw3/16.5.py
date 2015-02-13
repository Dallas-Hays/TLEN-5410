""" Dallas Hays
    Exercise 16.5
    Homework 3
"""

class Time(object):
    """ Represents the time of day.
        attributes: hour, minute, second
    """
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    """ Knowing about divmod would have made my solution to
        16.3 and 16.4 slightly easier
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def increment(time, seconds):
    """ Simple, convert time to seconds, add the seconds,and then
        convert back to a time value. Return the new incremented time
    """
    seconds += time_to_int(time)
    return int_to_time(seconds)

def main():
    t1 = Time()
    t1.hour = 11
    t1.minute = 59
    t1.second = 30

    t1 = increment(t1, 3629)
    print "%.2d:%.2d:%.2d" % (t1.hour, t1.minute, t1.second)

main()
