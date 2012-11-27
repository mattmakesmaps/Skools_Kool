__author__ = 'matt'

from os import walk

def vision_Quest(directory):
    """Use os.walk to print out file names in a given dir"""
    for root, dirs, files in walk(directory):
        print files

if __name__ == '__main__':
    print vision_Quest('/Users/matt/PycharmProjects/Skools_Kool')
