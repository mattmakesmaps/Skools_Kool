__author__ = 'matt'

"""
Write a program that searches a directory and all of its subdirectories, recursively, and returns a list of complete paths for all files with a given suffix (like .mp3). Hint: os.path provides several useful functions for manipulating file and path names.
"""

"""
To check for dups across the entire root dir and sub directories, i think you need to store all md5 checksums in an indexable file.
maybe dump results into a pickleable file, and can be used for search?
"""

from os import walk, path, popen

def checkSumCreator(file):
    cmd = 'md5 ' + file
    fp = popen(cmd)
    res = fp.read()
    stat = fp.close()
    position = res.rfind(' = ')
    return res[position+3:]

def fileFinder(rootDir, filetype):
    """Given a root directory and file type, return full paths for all matches"""
    checkSums = []
    fileLen = len(filetype)
    for root, dirs, files in walk(rootDir):
        for file in files:
            checkSums.append(checkSumCreator(file))
            if file[-fileLen:] == filetype:
                print path.join(root, file)

if __name__ == '__main__':
    print fileFinder('/Users/matt/PycharmProjects/Skools_Kool/Chapter14','py')
