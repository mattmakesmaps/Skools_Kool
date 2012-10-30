__author__ = 'matt'

"""
Write a program that searches a directory and all of its subdirectories, recursively, and returns a list of complete paths for all files with a given suffix (like .mp3). Hint: os.path provides several useful functions for manipulating file and path names.
"""

"""
To check for dups across the entire root dir and sub directories, i think you need to store all md5 checksums in an indexable file.
maybe dump results into a pickleable file, and can be used for search?
"""

import os
from collections import Counter

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
    """Given a root directory and file type, return a dictionary
    containing fullpaths as keys and checksums as values"""
    checkSums = {} # If storing just file names, can't see files with same name, different folder.
    fileLen = len(filetype)
    for root, dirs, files in os.walk(rootDir):
        for file in files:
            if file[-fileLen:] == filetype:
                csFile = checkSumCreator(file)
                checkSums[os.path.join(root, file)] = csFile[1]
    return checkSums

def findDupsViaDict(dicts):
    """Given a dictionary of file and md5s, identify dups using a counter pattern"""
    # Loop through completed dictionary using generator

    # Use a counter to ID dups
    # TODO currently fails quality check for checksums
    for key, value in dicts.iteritems():
        counter = 0
        if value in dicts.itervalues():
            counter+=1
        if counter > 1:
            print 'File has duplicate: %s' % key

def findDupsViaCounter(dicts):
    """Given a dictionary, identify dups using a collection.Counter() collection"""
    checkSumList = []
    # Create the counter
    """NOTE: If you pass iteritems() a single variable,
    that variable is assigned a 2 item tuple containing both
    the key and value"""
    for value in dicts.itervalues():
        checkSumList.append(value)
    checkSumCounter = Counter(checkSumList)

    for key, value in checkSumCounter.iteritems():
        if value > 1:
            print "Duplicate Checksum Found: %s" % key

if __name__ == '__main__':
    filesAndChecks = fileFinder('/Users/matt/PyCharmProjects/Skools_Kool/Chapter14','py')
    print filesAndChecks
    print "Begin Duplicate Check using findDupsViaDict()"
    findDupsViaDict(filesAndChecks)
    print "End Duplicate Check"
    print "Begin Dup Check using findDupsViaCounter()"
    findDupsViaCounter(filesAndChecks)
    print "End Duplicate Check"
