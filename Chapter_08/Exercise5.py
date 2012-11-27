__author__ = 'matt'

def count(word, letter):
    """Given a string and a letter,
    return occurence count"""
    counter = 0
    for i in word:
        if i==letter:
            counter+=1
    return counter

if __name__ == '__main__':
    print count('racecar', 'c')
    print count('racecar', 'e')
