__author__ = 'matt'

"""
Use get to write histogram more concisely. You should be able to eliminate the if statement.
"""

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogramGet(s):
    """For a given sequence, return a count of each element"""
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) # Need to assign default value '0' to key 'c' if not present in dict 'd'
        d[c] += 1
    return d

if __name__ == '__main__':
    print histogramGet('RileyJones')

