__author__ = 'matt'

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word [1:-1]

def is_palindrome(word):
    """
    Function returns boolean based on input string
    being a palindrome.
    """
    if first(word) != last(word):
        print "Not a palindrome"
        return False
    elif first(word) == last(word) and len(word) <= 3:
        return True
    elif first(word) == last(word):
        recurse = middle(word)
        return is_palindrome(recurse)
    else:
        print "error"
        return False

if __name__ == '__main__':
    """
    print middle('fourty')
    print middle('foo')
    print middle('to')
    print middle('t')
    print middle('')
    """
    print is_palindrome('racecar')
    print is_palindrome('noon')
    print is_palindrome('oo')
    print is_palindrome('Riley')
