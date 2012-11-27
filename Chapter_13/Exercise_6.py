__author__ = 'matt'
"""
Python provides a data structure called set that provides many common set operations. Read the documentation at http://docs.python.org/lib/types-set.html and write a program that uses set subtraction to find words in the book that are not in the word list. Solution: http://thinkpython.com/code/analyze_book2.py.
"""

import sys, string
from collections import OrderedDict

def processLine(stringin, setin):
    """For a given line, append to a dictionary individual words and counts"""
    line = stringin.strip()
    words = line.split()
    for word in words:
        # http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
        word = word.translate(string.maketrans("",""), string.punctuation + string.digits).lower()
        setin.add(word)
    return setin

def processFile(fin, processFunc):
    """Return a set of distinct words"""
    s = set()

    try:
        myFile = open(fin, 'r')
        for line in myFile.readlines():
            processFunc(line, s)

        return s

    except:
        e = sys.exc_info()
        print e

    finally:
        myFile.close()

if __name__ == '__main__':
    bookFile = '/Users/matt/Documents/PyCharm/Skools_Kool/Chapter_13/Books/moby_dick.txt'
    wordFile = '/Users/matt/Documents/PyCharm/Skools_Kool/Chapter_14/words.txt'
    bookWords = processFile(bookFile, processLine)
    wordWords = processFile(wordFile, processLine)

    # See for more set methods http://docs.python.org/2/library/stdtypes.html#set
    weirdBookWords = bookWords.difference(wordWords)
    print weirdBookWords
