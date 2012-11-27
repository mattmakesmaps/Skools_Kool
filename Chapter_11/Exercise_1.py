# coding=utf-8
__author__ = 'matt'

"""
Write a function that reads the words in words.txt and stores them as keys in a dictionary. It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.
"""

def has_word(fin, wordin):
    """Return True if word is present with a file"""
    fDict = {}
    file = open(fin, 'r')

    for line in file:
        fDict[line.strip()] = ''

    if wordin in fDict:
        return True
    return False

if __name__ == '__main__':
    print has_word('/Users/matt/Documents/PyCharm/Skools_Kool/Chapter_09/words2.txt', 'cat')
    print has_word('/Users/matt/Documents/PyCharm/Skools_Kool/Chapter_09/words2.txt', 'cat')

