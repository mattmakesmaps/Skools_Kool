__author__ = 'matt'
"""
An example of a dispatch table.
http://my.safaribooksonline.com/book/programming/python/0596007973/python-shortcuts/pythoncook2-chp-4-sect-16
"""

import sys

def double(a): return a * 2

def addFour(a): return a + 4

def minusEight(a): return a - 8

def square(a): return a ** 2

def breakMe(a): sys.exit()

tokenDict = {'exit': breakMe, '1': double, '2': addFour, '3': minusEight, '4': square}

# Use Lambda functions as an alternative
tokenDictLambda = {'double': lambda x:x*2,
                   'addFour': lambda x:x+4,
                   'minusEight': lambda x:x-8,
                   'square': lambda x:x**2,
                   'exit': breakMe}

def Triple(a):
    return a * 3

if __name__ == '__main__':
    while True:
        choice = raw_input('Select Operation >>> ')
        value = int(raw_input('Value is >>> '))
        if choice == 'add Triple()':
            tokenDictLambda['triple'] = Triple
        if choice in tokenDictLambda:
            print tokenDictLambda[choice](value)
        else:
            print "Oops, not a choice!"
