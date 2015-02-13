""" Dallas Hays
    Exercise 17.7
    Homework 4

    References:
    1. http://www.greenteapress.com/thinkpython/code/BadKangaroo.py
    For the object.__str__(self) notation of returning an objects string
    representation
"""

class Kangaroo(object):
    """ Kangaroo object """
    def __init__(self):
        """ Initialize to empty list """
        self.pouch_contents = []

    def put_in_pouch(self, any_type_object):
        """ Add new object to the pouch contents """
        self.pouch_contents.append(any_type_object)

    def __str__(self):
        """ Returns a string representation of the kangaroo
            object and the contents of its pouch
        """
        new_string = object.__str__(self) + " contains: "
        for objects in self.pouch_contents:
            next_object = object.__str__(objects) + " | "
            new_string += next_object
        return new_string

def main():
    roo = Kangaroo()
    kanga = Kangaroo()
    roo.put_in_pouch("some text")
    roo.put_in_pouch("more text")
    kanga.put_in_pouch(roo)

    print roo
    print kanga

main()
