# Dallas Hays
# 1/18/15
# Homework 1
# Exercises: 5.1, 6.2, 7.4, 8.1, 8.3, 8.10, 8.12
#
#
#
import math

# ---------------------------------------------------------------------

# Exercise 5.1
def print_n(s, n):
    if n <= 0:
        return
    print s
    print_n(s, n-1)
# Stack Diagram:
# <module> _____________________
# print_n  __n->2__s->'Hello'___
# print_n  __n->1__s->'Hello'___
# print_n  __n->0__s->'Hello'___

# ---------------------------------------------------------------------

# Exercise 6.2
# Iteration 1: Create the function and the main variables. Also
# add the return statement
def hypotenuse(len1, len2):
    len3 = 0.0
    return len3

# Iteration 2: Make the variables of the pythagorean theorem. Print
# their values to ensure they are created correctly
def hypotenuse(len1, len2):
    a = len1**2
    b = len2**2
    print "a squared is:", a
    print "b squared is:", b

    len3 = 0.0
    return len3

# Iteration 3: Add the values together to get the hypotnuse leg squared.
# Print it to make sure that it is working
def hypotenuse(len1, len2):
    a = len1**2
    b = len2**2
    c = a + b
    print "c squared is:", c

    len3 = 0.0
    return len3
# Iteration 4: Need to import math so that we can find the square root
# of c. This value will be the length of the hypotnuse so we return
# the value. Use print statement to ensure that it works correctly
def hypotenuse(len1, len2):
    a = len1**2
    b = len2**2
    c = a + b
    len3 = math.sqrt(c)
    return len3

# print hypotenuse(3, 4)

# ---------------------------------------------------------------------

# Exercise 7.4
# Uses raw_input to request input from the user to be evaluated. Prints
# the result. If the user types in 'done' then the function will end
# and return the last value of result. Result defaults to 0.0 in case
# the first input is done.
def eval_loop():
    print "Evaluate an expression, type 'done' to end."
    result = 0.0
    while(True):
        equation = raw_input("What do you want to evaluate? ")
        if equation == 'done':
            return result
        else:
            result = eval(equation)
            print result

# eval_loop()
# ---------------------------------------------------------------------

# Exercise 8.1
# Prints the string in reverse, one letter per line
# I tried to not use a for loop or the reverse method because I don't
# think they wanted you to at this point of the book

def reverse_letters(word):
    index = len(word) - 1
    while index >= 0:
        letter = word[index]
        print letter
        index -= 1

# reverse_letters('word')

# ---------------------------------------------------------------------

# Exercise 8.3
# The [n:m] notation means return the n to m part of the string. So
# if n is 3 and m is not defined, then the last 3 letters of the fruit
# string will be returned. That means if we do not have either
# n or m that the whole string will be printed instead.

#fruit = 'banana'
#print fruit[3:] -> will print ana

# ---------------------------------------------------------------------

# Exercise 8.10
# The 6.6 version...
# def is_palindrome(word):
#    """Returns True if word is a palindrome."""
#    if len(word) <= 1:
#        return True
#    if first(word) != last(word):
#        return False
#    return is_palindrome(middle(word))
#
# A simple if statement to check if word is the same forward and
# backwards.

def is_palindrome(word):
    if (word == word[::-1]):
        return True
    else:
        return False

# print is_palindrome('test')
# print is_palindrome('civic')

# ---------------------------------------------------------------------

# Exercise 8.12
# Rotate the letters of a word by some value
#

def rotate_word(word, shift):
    shift = shift % 26     # Use modulo to always have forward movement
    new_word = ''          # Blank strings can add letters to them
    j = 0                  # Iterator
    for i in word:
    # Use ord to convert letters to numbers, and chr to change them back
        if (ord(i) + shift > 122):
            new_word += chr(ord(i) + shift - 26)
        else:
            new_word += chr(ord(i) + shift)
        j += 1

    print new_word

# rotate_word('melon', -10)
# rotate_word('cheer', 7)

"""
# Initially I used lists, but changed to just strings.

# Rotate the letters of word by the value of shift. Uses modulo on shift
# so that the value is always 0-25. I use lists because they are mutable
# and easier than strings in this case. Uses ords to convert letters to
# numbers and then chr to convert the number back to a letter

def rotate_word(word, shift):
    shift = shift % 26     # Use modulo to always have forward movement
    new_word = list(word)  # Lists are mutable, easier than strings
    j = 0                  # Iterator
    for i in word:
        if (ord(i) + shift > 122):
            new_word[j] = chr(ord(i) + shift - 26)
        else:
            new_word[j] = chr(ord(i) + shift)
        j += 1

    print "".join(new_word)
"""
