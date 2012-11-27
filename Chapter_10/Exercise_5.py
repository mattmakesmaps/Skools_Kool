__author__ = 'matt'

"""
Write a function called chop that takes a list, modifies it by removing the first and last elements, and returns None.
"""

def chop(inlist):
    inlocallist = inlist[1:-1]
    print inlocallist

if __name__ == '__main__':
    onelist = [1,2,3,4,5,6]
    print onelist
    print chop(onelist)
    print onelist
