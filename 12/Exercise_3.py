__author__ = 'matt'

"""
Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. Find text samples from several different languages and see how letter frequency varies between languages. Compare your results with the tables at http://en.wikipedia.org/wiki/Letter_frequencies. Solution: http://thinkpython.com/code/most_frequenct.py.
"""

def most_frequent(instring):
    dictCount = {}
    for letter in instring:
        if letter in dictCount:
            dictCount[letter] += 1
        else:
            dictCount[letter] = 1

    tupleCount = dictCount.items()
#    for i in tupleCount:
         # I guess tuple assignment doesn't work for tuples
#        i[0],i[1] = i[1],i[0]

    # What the hell did I just do?
    tupleCount.sort(key=lambda letter: letter[1], reverse=True)

    sortedList = []
    for eachTuple in tupleCount:
        sortedList.append(eachTuple[0])

    return sortedList

if __name__ == '__main__':
    print most_frequent('hannabarberra')
