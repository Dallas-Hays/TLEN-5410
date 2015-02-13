""" Dallas Hays
    1/23/15
    Homework 2
    Exercises 10.6, 10.8(part 1 ONLY), 11.9, 14.6
"""
import urllib


""" Exercise 10.6:
    First check the length of the list to make sure it is at least of size
    1 or not. Then iterate through it until the second to last member of
    the list (len(some_list)-1). Then do a simple comparison to see if
    the current value is larger than the next value.

    Resources:
    http://stackoverflow.com/questions/1712227/how-to-get-the-size-of-a-list
    Length of lists

    http://stackoverflow.com/questions/9450446/how-do-i-use-a-c-style-for-loop-in-python
    How to iterate similar to C in python
"""
def is_sorted(some_list):
    if len(some_list) > 1:
        for i in range(0, len(some_list)-1):
            if some_list[i] > some_list[i+1]:
                return False
        return True

#print is_sorted([1,2,3,4,5,6,7,8,9])
#print is_sorted([1,2,3,4,5,6,7,8,9,0])
#print is_sorted(['a', 'b', 'c'])
#print is_sorted(['a', 'b', 'c', 'z', 'a'])

""" Exercise 10.8:
    Not very elegant, but it works. Basically nested for loops that both iterate
    over the list, comparing values of the two iterations. I increment a variable
    k if there is a same value. If k increments to 2, then that means there is
    a duplicate so return true.
"""

def has_duplicates(mylist):
    for i in range(0, len(mylist)-1):
        k = 0
        for j in range(0, len(mylist)):
            if mylist[j] == mylist[i]:
                k+=1
            if k >= 2:
                return True
    return False

#print has_duplicates([1,2,3,4,5,6,7,8,9,0,1,2])
#print has_duplicates([1,2,3,4,5,6,7,8,9,0])

""" Exercise 11.9
    Uses a dictionary to find duplicates in the list. Iterates using the values
    in the list, and checks if those keys have some value associated with them.
    If they do not then it will set the value of the key to True, if it is in
    the dictionary then it will return True.

    Resources:
    http://www.greenteapress.com/thinkpython/code/has_duplicates.py
    I didn't really understand dictionaries so I used to solution to help
"""
def has_duplicates2(mylist):
    mydict = dict()
    for i in mylist:
        if i in mydict:
            return True
        else:
            mydict[i] = True
    return False

#print has_duplicates2([1,2,3,4,5,6,7,8,9,0,1,2])
#print has_duplicates2([1,2,3,4,5,6,7,8,9,0])



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

def zipcode():
    zc = raw_input("Please input a zipcode:")
    conn = urllib.urlopen("http://www.uszip.com/zip/"+ zc)

    # Finds the total population
    htmlsource = conn.read()
    val = htmlsource.find("Total population</dt><dd>")
    print "Total population: " + htmlsource[val+25:val+60].partition("<")[0]

    # Finds the city name
    val2 = htmlsource.find("is the ZIP code for ")
    print "City: " + htmlsource[val2+20:val2+60].partition("?")[0]

zipcode()
