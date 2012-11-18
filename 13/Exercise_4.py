__author__ = 'matt'
"""
Modify the previous program to read a word list (see Section 9.1) and then print all the words in the book that are not in the word list. How many of them are typos? How many of them are common words that should be in the word list, and how many of them are really obscure?
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

        return sortedDict, distinctWords

    except:
        e = sys.exc_info()
        print e
    finally:
        myFile.close()

if __name__ == '__main__':
    bookFile = '/Users/matt/Documents/PyCharm/Skools_Kool/13/Books/moby_dick.txt'
    wordFile = '/Users/matt/Documents/PyCharm/Skools_Kool/14/words.txt'
    bookWords, bookDistinctWords = processFile(bookFile, processLine)
    wordWords, wordDistinctWords = processFile(wordFile, processLine)

    # From the list of book words, delete those that appear in main word list.
    for key in bookWords.iterkeys():
        if key in wordWords:
            bookWords.pop(key=key)

    print bookWords
