__author__ = 'matt'
"""
Type this example into a file named wc.py and run it as a script. Then run the Python interpreter and import wc. What is the value of __name__ when the module is being imported?
"""
import os, sys

def linecount(filename):
    count = 0
    for line in open(filename):
        count+=1
    return count

if __name__=='__main__':
    # Use sys.path.insert to add directory to python path
    sys.path.insert(0,'/home/matt/projects/Skools_Kool/Chapter14/')
    print __name__
    import wc
    print __name__
    print os.getcwd()
    print linecount('/home/matt/projects/Skools_Kool/Chapter14/wc.py')
