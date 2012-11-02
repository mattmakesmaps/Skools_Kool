__author__ = 'matt'

"""
Write a function that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i+1 elements from the original list. For example, the cumulative sum of [1, 2, 3] is [1, 3, 6].
"""

def runsum(numlist):
    for i in range(len(numlist)):
        if i == 0: #Otherwise first index will be added to last index [-1]
            numlist[i] = numlist[i]
        else:
            numlist[i] = numlist[i]+numlist[i-1]
    return numlist

if __name__ == '__main__':
    listin = [1,2,3]
    print runsum(listin)
