# coding=utf-8
__author__ = 'matt'

def avoids(word, bad_letters):
    """Take a word, and return True if
        word doesn't contain any forbidden letters"""
    # Using while loop
    i = 0
    while i < len(word):
        if word[i] in bad_letters:
            return False
        else:
            i+=1
    return True

def avoids_RawInput(in_file):
    """Prompt User Input for forbidden letter list
    check against word list"""
    bad_letters = raw_input('bad letters >>>').split(',')
    fin = open(in_file, 'r')

    goodWordCount=0
    for line in fin:
        if avoids(line.strip(), bad_letters):
            goodWordCount+=1
    return goodWordCount

# Exercise 4
def uses_only(word, only_letters):
    """Write a function named uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the list. Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa?”"""
    i = 0
    while i <len(word):
        if word[i] in only_letters:
            i+=1
        else:
            return False
    return True

# Exercise 5
def uses_all(word, required_letters):
    """Write a function named uses_all that takes a word and a string of required letters, and that returns True if the word uses all the required letters at least once."""
    for letter in required_letters:
        if letter not in word: # Using not in since we need this to happen only once
            return False
    return True # Only want to return true after all required letters have been confirmed used

# Exercise 6
def is_abcedarian(word):
    """Write a function called is_abecedarian that returns True if the letters in a word appear in alphabetical order (double letters are ok)."""
    splitter = []
    for letter in word:
        splitter.append(letter)
    # sorted = splitter.sort()
    # For whatever reason, above code won't assign a sorted instance of list splitter to sorted
    # but rather will go ahead and sort splitter, and return sorted is None
    # OK What's happening is that the list is being aliased, not cloned.
    # http://www.greenteapress.com/thinkpython/thinkCSpy/html/chap08.html see 8.Chapter_11-8.Chapter_12
    sorted = splitter[:] # clone that shit, with a slice
    sorted.sort()
    if splitter == sorted:
        return True
    else:
        return False


if __name__ == '__main__':
    #bad_letters = ['a','c','d']
    #print avoids('june', bad_letters)
    #print avoids('jam',bad_letters)
    #print avoids_RawInput('words2.txt')
    #print uses_only('racecar',['r','a','c','e'])
    #print uses_only('racecar',['z'])
    #print uses_all('racecar',['r','a'])
    #print uses_all('racecar',['r','a','z'])
    print is_abcedarian('abcxyz')
    print is_abcedarian('ztxe')