""" Dallas Hays
    2/16/15
    Homework 1
    Exercise 8.1, 8.12
"""
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

def main():
    reverse_letters('word')
    rotate_word('melon', -10)
    rotate_word('cheer', 7)

if __name__ == "__main__":
    main()
