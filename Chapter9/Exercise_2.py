__author__ = 'matt'

def has_no_e(word):
    """Returns True if input has no 'e'"""
    for i in word:
        if i=='e':
            return False
    return True

def has_no_e_list(in_list):
    """take a list, and print words w/o 'e'"""
    fin = open(in_list, 'r')
    noECount = 0
    lineCount = 0
    for line in fin:
        lineCount+=1
        if has_no_e(line):
            print line
            noECount+=1
    print str((float(noECount)/float(lineCount))*100)

if __name__ == '__main__':
    #print has_no_e('word')
    #print has_no_e('gave')
    has_no_e_list('words.txt')
