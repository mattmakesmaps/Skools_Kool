__author__ = 'matt'

"""
In this example, ties are broken by comparing words, so words with the same length appear in reverse alphabetical order. For other applications you might want to break ties at random. Modify this example so that words with the same length appear in random order. Hint: see the random function in the random module. Solution: http://thinkpython.com/code/unstable_sort.py.
"""

from random import random

def sort_by_length(words):
    t = []
    for word in words:
#        Append with a tuple containg elements for length and the word
        t.append((len(word), random(), word))
#        t.append((random(),len(word), word))

    # For a tuple, sort occurs based on elements from left to right
    t.sort(reverse=True)

    # Identify tuples with the same length
    # Append a third random value to all dup length values
    # Append value of 0 to all non-dups
    ## Oh wait don't need to do all this crap ^^^^^^^^^^^^
    ## because i can just salt with a random number,
    ## and all elements with a no matching lengths will be
    ## sorted by length first

    res = []
    for length, dupsort, word in t:

        res.append(word)
    return res

if __name__ == '__main__':
    sortSequence = ('cat','rat','matt','fence','hair','chair')
    print sort_by_length(sortSequence)
