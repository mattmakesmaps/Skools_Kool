__author__ = 'matt'

prefix = 'JKLMNOPQ'
suffix = 'ack'
badLetters = ['Q','O']

for letter in prefix:
    if letter not in badLetters:
        print letter + suffix
    elif letter in badLetters:
        print letter + 'u' + suffix
    else:
        print "error"
