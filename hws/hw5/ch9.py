""" Dallas Hays
    2/16/15
    Homework 1
    Exercise 9.1

    References:
    http://stackoverflow.com/questions/16922214/reading-a-text-file-and-
    splitting-it-into-single-words-in-python
    For reminding me about the split() method for lists

    I couldn't get the...

    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        print word

    Example to work, so I needed to use lists
"""

def over_twenty():
    fin = open('words.txt', 'r')
    for word in fin.read().split():
        if len(word) > 20:
            print word

def main():
    over_twenty()

if __name__ == "__main__":
    main()
