__author__ = 'matt'

"""
Write a program that searches a directory and all of its subdirectories, recursively, and returns a list of complete paths for all files with a given suffix (like .mp3). Hint: os.path provides several useful functions for manipulating file and path names.
"""

"""
To check for dups across the entire root dir and sub directories, i think you need to store all md5 checksums in an indexable file.
maybe dump results into a pickleable file, and can be used for search?
"""

import os

def checkSumCreator(file):
    """Returns a list with the file name and checksum for a given file"""
    cmd = 'md5 ' + file
    fp = os.popen(cmd)
    res = fp.read()
    stat = fp.close()
    position = res.rfind(' = ')
    checkSum = res[position+3:].strip()
    fileName = res[5:position-1]
    return [fileName,checkSum]

def fileFinder(rootDir, filetype):
    """Given a root directory and file type, return full paths for all matches"""
    checkSums = {}
    fileLen = len(filetype)
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            if file[-fileLen:] == filetype:
                csFile = checkSumCreator(file)
                checkSums[os.path.join(root, file)] = csFile[1]
    return checkSums

def findDups(dicts):
    """Given a dictionary of file and md5s, identify dups"""
    # Loop through completed dictionary using generator
    for key, value in dicts.iteritems():
        counter = 0
        if value in dicts.values():
            counter+=1
        if counter > 1:
            print 'File has duplicate: %s' % key

if __name__ == '__main__':
    filesAndChecks = fileFinder('/Users/matt/PycharmProjects/Skools_Kool/Chapter14','py')
    print filesAndChecks
    print "Begin Duplicate Check"
    findDups(filesAndChecks)
    print "End Duplicate Check"
