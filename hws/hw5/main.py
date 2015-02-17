""" Dallas Hays
    2/16/15
    Homework 5

    NOTE TO GRADER:
    When run, type the name of the function     EG: is_sorted
    Then, it may or may not prompt you for input, respond accordingly

    References:
    1. http://stackoverflow.com/questions/2349991/python-how-to-import-other-
    python-files
    This for how to import local python files

    2. http://stackoverflow.com/questions/7368789/convert-all-strings-in-a-
    list-to-int
    For how to use the map function to convert a list of strings to integers
"""

from ch6 import hypotenuse
from ch7 import eval_loop
from ch8 import reverse_letters, rotate_word
from ch9 import over_twenty
from ch10 import is_sorted
from ch14 import zipcode


def chosen(choice):
    """ Function that will perform the functions from the other files.
        Fairly straightforward, some changes were necessary to allow for
        input (is_sorted asks you to give it a list of values)
    """

    var = []    # Empty list to be used for arguments to the functions
    if choice == "hypotenuse":
        var.append(float(raw_input("Please enter the first variable: ")))
        var.append(float(raw_input("Please enter the second variable: ")))
        print hypotenuse(var[0], var[1])
    elif choice == "eval_loop":
        eval_loop()
    elif choice == "reverse_letters":
        var.append(raw_input("Please enter the word: "))
        reverse_letters(var[0])
    elif choice == "rotate_word":
        var.append(raw_input("Please enter the word: "))
        var.append(int(raw_input("Please enter the shift value: ")))
        print rotate_word(var[0], var[1])
    elif choice == "over_twenty":
        over_twenty()
    elif choice == "is_sorted":
        not_done = True
        print "Enter values to be added to a list"
        print "When finished, please type 'done'\n"
        while not_done:
            var.append(raw_input("Please enter ONLY numbers for the list: "))
            if var[-1] == "done":
                var.pop()
                var = map(int, var)
                not_done = False
                print is_sorted(var)
    elif choice == "zipcode":
        zipcode()
    else:
        print "Next time choose a valid function!"

def main():
    print "Functions: hypotenuse, eval_loop, reverse_letters, rotate_word"
    print "over_twenty, is_sorted, zipcode\n"

    choice = raw_input("Which function would you like to run? ")

    chosen(choice)


if __name__ == "__main__":
    main()
