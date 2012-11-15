__author__ = 'matt'

"""
If you did Exercise 10.8, you already have a function named has_duplicates that takes a list as a parameter and returns True if there is any object that appears more than once in the list.
Use a dictionary to write a faster, simpler version of has_duplicates. Solution: http://thinkpython.com/code/has_duplicates.py.
"""

def has_duplicates(listin):
    """Return True if input has duplicates. Can probably shorten using ternary"""
    counterDict = {}
    for element in listin:
        if element in  counterDict:
            return True
        else:
            counterDict[element] = 1
    return False

if __name__ == '__main__':
    goodList = ['matt', 'pat', 'cat']
    badList = ['matt', 'matt','pat', 'cat']
    print has_duplicates(goodList)
    print has_duplicates(badList)

