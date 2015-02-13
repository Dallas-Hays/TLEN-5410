""" Dallas Hays
    Exercise 16.7 part 1
    Homework 3

    References:
    https://docs.python.org/2/library/datetime.html
    How to use datetime
"""

import datetime

def main():
    weekdays = ["Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday"]

    print "The date is: " + str(datetime.date.today())
    print "The day of the week is: " + weekdays[datetime.date.today().weekday()]

main()
