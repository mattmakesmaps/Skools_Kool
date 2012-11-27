__author__ = 'matt'

"""
Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. So middle([1,2,3,4]) should return [2,3].
"""

def middle(inlist):
    return inlist[1:-1]

if __name__ == '__main__':
    onelist = [1,2,3,4,5,6]
    print middle(onelist)
