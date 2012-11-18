__author__ = 'matt'
"""
Modify the program from the previous exercise to print the 20 most frequently-used words in the book.
"""

import sys, string
from collections import OrderedDict

def processLine(sin, din):
    """For a given line, append to a dictionary individual words and counts"""
    line = sin.strip()
    words = line.split()
    for word in words:
        # http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
        word = word.translate(string.maketrans("",""), string.punctuation).lower()
        # Use get method to check for key. If key is not present, use value of 0.
        # Reassign new key value
        din[word] = 1 + din.get(word, 0)
    return din


def processFile(fin, processFunc):
    """Return an ordered dictionary of distinct words and occurance counts, along with total word count"""
    d = dict()

    try:
        myFile = open(fin, 'r')
        for line in myFile.readlines():
            processFunc(line, d)
        distinctWords = len(d) # Get a distinct word count.
        # Create an OrderedDictionary. Use t[0] to sort by key, use t[1] to sort by value.
        sortedDict = OrderedDict(sorted(d.items(), key=lambda t: t[1]))

        # Pop out twenty most frequently used words.
        topTwentyWords = []
        while len(topTwentyWords) < 20:
            topTwentyWords.append(sortedDict.popitem()) # popitem defaults to return last record first (FILO)
        return topTwentyWords, distinctWords

    except:
        e = sys.exc_info()
        print e
    finally:
        myFile.close()

if __name__ == '__main__':
    bookFile = '/Users/matt/Documents/PyCharm/Skools_Kool/13/Books/moby_dick.txt'
    infile = '/Users/matt/Documents/PyCharm/Skools_Kool/13/testtext.txt'
    topTwentyWords, distinctWordCount = processFile(bookFile, processLine)
    print distinctWordCount
    print topTwentyWords

