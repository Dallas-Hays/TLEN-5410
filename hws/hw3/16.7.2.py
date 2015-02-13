""" Dallas Hays
    Exercise 16.7 part 2
    Homework 3

    References:

    http://stackoverflow.com/questions/5294314/python-get-number-of-years-that
    -have-passed-from-date-string
    For calc_age logic

    http://www.greenteapress.com/thinkpython/code/Time1_soln.py
    For time until birthday
"""

from datetime import datetime

def calc_age(bday):
    """ Calculate the age of the birthdate
        Finds the amount of days since the birthday, and converts it to
        years and returns the value
    """
    before = datetime.strptime(bday, '%Y-%m-%d')
    now = datetime.now()
    return int((now-before).days/365.25)


def days_until_bday(bday):
    """ Compares the bday with today's date. If the birthday has already past
        this year then we need to calculate with respect to their birthday next
        year.
    """
    today = datetime.today()
    next_bday = datetime(today.year, bday.month, bday.day)
    if today > next_bday:
        next_bday = datetime(today.year+1, bday.month, bday.day)
    days_til = next_bday - today
    print "Time until next bday: "
    print days_til


def main():
    print "Format: year-month-day   Remember the '-'"
    bday = raw_input("Please enter a birthday: ")
    bday_list = bday.split("-")
    datetime_bday = datetime(int(bday_list[0]),
                             int(bday_list[1]),
                             int(bday_list[2]))

    age = calc_age(bday)
    print "Age is: "+ str(age)

    days_until_bday(datetime_bday)

main()
