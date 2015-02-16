""" Dallas Hays
    2/16/15
    Homework 5

    References:
    1. http://stackoverflow.com/questions/2349991/python-how-to-import-other-
    python-files
    This for how to import local python files
"""

from ch6 import hypotenuse
from ch7 import eval_loop
from ch8 import reverse_letters, rotate_word
from ch9 import over_twenty
from ch10 import is_sorted
from ch14 import zipcode

def main():
    choice = raw_input("Which function would you like to run? ")
    var = [] # List for arguments to the functions
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
        print "When finished, please type 'done' "
        while not_done:
            var.append(raw_input("Please enter something for the list: "))
            if var[-1] == "done":
                var.pop()
                not_done = False
                print is_sorted(var)
    elif choice == "zipcode":
        zipcode()


if __name__ == "__main__":
    main()
