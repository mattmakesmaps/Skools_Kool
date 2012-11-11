__author__ = 'matt'

"""
Modify print_hist to print the keys and their values in alphabetical order.
"""

def print_hist(h):
    for c in h:
        print c, h[c]

def print_hist_alpha(h):
    """Return in alphabetical order keys and values for a given dict."""
    alpha_keys = h.keys()
    alpha_keys.sort()

    for i in alpha_keys:
        print i, h[i]

if __name__ == '__main__':
    mattDict = {'z': 200, 'x':'letter', 'a': 30, 25:'number'}
    print print_hist_alpha(mattDict)