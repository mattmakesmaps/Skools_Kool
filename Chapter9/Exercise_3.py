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
        i = 0
        while i < len(line):
            if line[i] in bad_letters:
                break
            goodWordCount+=1
            i+=1
    return goodWordCount



if __name__ == '__main__':
    #bad_letters = ['a','c','d']
    #print avoids('june', bad_letters)
    #print avoids('jam',bad_letters)
    print avoids_RawInput('words2.txt')