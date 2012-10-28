__author__ = 'matt'

from string import count

def countMe(s, sub, start=None, end=None):
    """Mimic functionality of string.count() method"""
    # Test for values in star/end
    if end is None:
        end = len(s)

    if start is None:
        index = 0
    else:
        index = start

    countMeCount = 0
    while index < end:
        if s[index]==sub:
            countMeCount+=1
            index+=1
        else:
            index+=1
    return countMeCount

if __name__ == '__main__':
    print countMe('racecar','c',2,5)

