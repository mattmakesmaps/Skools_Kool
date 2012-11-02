__author__ = 'matt'

"""
Write a function called is_sorted that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise. You can assume (as a precondition) that the elements of the list can be compared with the relational operators <, >, etc.
For example, is_sorted([1,2,2]) should return True and is_sorted(['b','a']) should return False.
"""

def is_sorted(inlist):
    # Make a copy of the list
    backupList = inlist[:]
    # Sort the COPY; NOT ORIGINAL
    backupList.sort()
    print inlist
    print backupList
    # Return true/false
    return backupList == inlist

def is_sortedMethod(inlist):
    # Use builtin method sorted()
    comparelist = sorted(inlist)
    print inlist
    print comparelist
    return inlist == comparelist

if __name__ == '__main__':
    unsorted = [3,1,4]
    print "pre execution: %s" % unsorted
    print is_sortedMethod(unsorted)
    print "post execution: %s" % unsorted
