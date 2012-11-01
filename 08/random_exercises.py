__author__ = 'matt'

def find(word,letter):
    """return index for a given letter in
    a given word. question, return all or first?
    answer. first
    """
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        else:
            index+=1
    return -1

if __name__ == '__main__':
    print find('racecar', 'c')
