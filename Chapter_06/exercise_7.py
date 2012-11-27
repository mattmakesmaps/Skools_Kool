__author__ = 'matt'
"""
A number, a, is a power of b if it is divisible by b and a/b is a power of b. Write a function called is_power that takes parameters a and b and returns True if a is a power of b. Note: you will have to think about the base case.
"""

def is_power(a,b):
    """Returns True if a is a power of b."""
    if a == b:
        print "divisible"
        return True
    elif a % b == 0:
        return is_power(a/b,b)
    else:
        print "not divisible"
        return False

if __name__ == '__main__':
    print is_power(1024,4)
    #print "\n"
    #print is_power(4,Chapter_16)
