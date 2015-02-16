""" Dallas Hays
    2/16/15
    Homework 1
    Exercise 6.2
"""

import math

# Exercise 6.2
def hypotenuse(len1, len2):
    a = len1**2
    b = len2**2
    c = a + b
    len3 = math.sqrt(c)
    return len3

def main():
    print hypotenuse(3.0, 4.0)

if __name__ == "__main__":
    main()
