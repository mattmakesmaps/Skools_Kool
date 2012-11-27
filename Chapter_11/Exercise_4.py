__author__ = 'matt'

"""
Modify reverse_lookup so that it builds and returns a list of all keys that map to v, or an empty list if there are none.
"""

def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise ValueError

def reverse_lookup_List(d, v):
    """Return a list containing all keys matching a given dictionary value."""
    klist = list()
    for k in d:
        if d[k] == v:
            klist.append(k)
    return klist

if __name__ == '__main__':
    mattDict = {'too-hundred':200, 'z': 200, 'x':'letter', 'a': 30, 25:'number'}
    print reverse_lookup_List(mattDict, 'letter')
    print reverse_lookup_List(mattDict, 200)
    print reverse_lookup_List(mattDict, 'novalue')

