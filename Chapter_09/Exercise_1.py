__author__ = 'matt'

def print20(in_file):
    """Take a file and print out only words
    over twenty characters in length
    """
    fin = open(in_file, 'r')
    for line in fin:
        if len(line.strip()) > 20:
            print line

if __name__ == '__main__':
    print20('words.txt')
