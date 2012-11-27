__author__ = 'matt'

def is_palindrome(word):
    return True if word==word[::-1] else False

if __name__ == '__main__':
    print is_palindrome('amazon')
    print is_palindrome('racecar')
