__author__ = 'matt'

"""
Write a function called sed that takes as arguments a pattern string, a replacement string, and two filenames; it should read the first file and write the contents into the second file (creating it if necessary). If the pattern string appears anywhere in the file, it should be replaced with the replacement string.
"""

import os

def sed(pattern, replacement, fin, fout):
    # Open File One
    finMem = open(fin)

    # Write Contents to File Two
    foutMem = open(fout, 'w+')

    # Search and replace string
    for line in finMem:
        if pattern in line:
            print 'pattern found'
            # Don't think it's possible to use list = list.replace()
            # TODO Investigate further
            newLine = line.replace(pattern,replacement)
            foutMem.write(newLine)
        else:
            foutMem.write(line)

if __name__ == '__main__':
    print os.getcwd()
    pattern = 'oy'
    replacement = 'it'
    fin = "/home/matt/projects/Skools_Kool/Chapter14/Exercise2_Test.txt"
    fout = "/home/matt/projects/Skools_Kool/Chapter14/Exercise2_Out.txt"
    sed(pattern, replacement, fin, fout)
