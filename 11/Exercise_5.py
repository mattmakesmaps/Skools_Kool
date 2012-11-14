__author__ = 'matt'

"""
Read the documentation of the dictionary method setdefault and use it to write a more concise version of invert_dict. Solution: http://thinkpython.com/code/invert_dict.py.
"""

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key] # Create a singleton, a one item list
        else:
            inverse[val].append(key) # We've seen this source value, append the additional key
    return inverse

def invert_dict_setdefault(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []) # check fo existence of val; Create singleton if not in inverse
        inverse[val].append(key) # Append source key as new inverse value
    return inverse

def invert_dict_Book(d):
    # From the book
    """Inverts a dictionary, returning a map from val to a list of keys.

    If the mapping key->val appears in d, then in the new dictionary
    val maps to a list that includes key.

    d: dict

    Returns: dict
    """
    inverse = {}
    for key, val in d.iteritems(): # iteritems negates needing to search for a value based on a key
        inverse.setdefault(val, []).append(key) # setdefault acts as a conditional test in a way
    return inverse

if __name__ == '__main__':
    mattDict = {'a': 1, 'p': 1, 'r': 2, 't': 1, 'o': 1}
    print invert_dict_setdefault(mattDict)
