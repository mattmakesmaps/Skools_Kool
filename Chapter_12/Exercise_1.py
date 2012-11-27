__author__ = 'matt'
"""
Write a function called sumall that takes any number of arguments and returns their sum.
"""

def sumall(*args):
    """Return sum of all arguments"""
    return sum(args)

if __name__ == '__main__':
    print sumall(0,1,2,3,4)