__author__ = 'matt'

import os, pwd

if __name__ == '__main__':

    try:
        print os.getcwd()
        # Test for file existence
        print os.access(os.getcwd(), os.F_OK)
        # Reccomended way of getting user name
        # Source http://docs.python.org/2/library/os.html#os.getlogin
        print pwd.getpwuid(os.getuid())
    finally:
        print "Cleanup"