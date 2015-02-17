""" Dallas Hays
    2/16/15
    Homework 1
    Exercise 10.6

"""

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

def main():
    my_list = [1, 5, 12, 3]
    print is_sorted(my_list)

if __name__ == "__main__":
    main()
