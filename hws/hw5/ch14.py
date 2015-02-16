""" Dallas Hays
    2/16/15
    Homework 1
    Exercise 14.6

"""

""" Exercise 14.6
    Write a program that prompts the user for a zip code and prints the
    name and population of the corresponding town.

    Val is the position where Total population begins in the html, val+25 is
    exactly when the numbers of the population begin, 60 was just an arbitrary
    large number, no other significance. This felt like a very hacky solution
    but I couldn't think of another way without some parsing library.

    Resources:
    1. http://www.diveintopython.net/html_processing/extracting_data.html
    Used to convert the html to a string

    2. http://stackoverflow.com/questions/8162021/analyzing-string-input-until-
    it-reaches-a-certain-letter-on-python
    This was for how to use the partition method to read a line until a certain
    character stops the reading
"""

import urllib

def zipcode():
    zc = raw_input("Please input a zipcode: ")
    conn = urllib.urlopen("http://www.uszip.com/zip/"+ zc)

    # Finds the total population
    htmlsource = conn.read()
    val = htmlsource.find("Total population</dt><dd>")
    print "Total population: " + htmlsource[val+25:val+60].partition("<")[0]

    # Finds the city name
    val2 = htmlsource.find("is the ZIP code for ")
    print "City: " + htmlsource[val2+20:val2+60].partition("?")[0]

def main():
    zipcode()

if __name__ == "__main__":
    main()
