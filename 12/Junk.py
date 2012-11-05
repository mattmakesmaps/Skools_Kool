__author__ = 'matt'

def has_match(t1, t2):
    """Return True if there is an index such that t1[i] == t2[i]"""
    for x,y in zip(t1,t2):
        if x == y:
            return True
    else:
        return False

def tuple_assignment():
    """Looking at tuple assignment for dictionary traversal"""
    phonebook = {}
    phonebook['Kenny','Matt'] = '555-5555-5550'
    phonebook['Kenny','Pat'] = '555-5555-5551'
    phonebook['Jones','Riley'] = '555-5555-5552'
    phonebook['Stewart','Matt'] = '555-5555-5553'

    for last, first in phonebook:
        print last, first, phonebook[last,first]

## Reports "ValueError: too many values to unpack"
#    for last, in phonebook:
#        print last, phonebook[last]

    print phonebook.keys()

if __name__ == '__main__':
    print has_match([0,1,4,8,'a'],[1,3,4,5,'a'])
    print has_match((0,1,4,8,'a'),(1,3,4,5,'a'))
    print has_match('matt','cat') # A String Is A Sequence.

    tuple_assignment()