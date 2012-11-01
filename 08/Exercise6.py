__author__ = 'matt'

# Exercise 4

def find(word,letter, index=0):
    """return index for a given letter in
    a given word. question, return all or first?
    answer. first

    Modify to have a third parameter denoting a start index
    """
    while index < len(word):
        if word[index] == letter:
            return index
        else:
            index+=1
    return -1

# Exercise 5

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

# Exercise 6

def countThreeParam(word,letter,index=0):
    counter = 0
    while index < len(word):
        if word[index] == letter:
            counter+=1
            index +=1
        else:
            index+=1
    return counter

if __name__ == '__main__':
    print countThreeParam('racecar','a')
    print countThreeParam('racecar','a',2)
