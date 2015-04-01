""" Dallas Hays
"""

import os
import flowd
import sys


def chooseFile():
    print "Files available in directory: \n"+' \n'.join(os.listdir('.'))
    print ""
    while(True):
        input = raw_input("Enter the Netflow file to analyze: ")
        if os.path.isfile(input):
            return input
        else:
            print input, "does not exist in the current directory."


def main():
    input = chooseFile()
    print input




if __name__ == "__main__":
    main()

