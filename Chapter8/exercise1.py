__author__ = 'matt'

"""
Write a function that takes a string as an argument and displays the letters backward, one per line.
"""

def backward(z):
    """
    Take a string and display letters backwards
    """
    index = 1
    while index < len(z):
        letter = z[-index]
        print letter
        index = index + 1
    print z[0] # Is there a better way? Seems hackish to have this at end.

if __name__ == '__main__':
    print backward('sometexthereyeah')