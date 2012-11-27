__author__ = 'matt'

"""
Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.
"""

def has_duplicates(inList):
    """Search Pattern for duplicate values in a list"""
    compareList=inList[:]
    compareList.sort()
    for i in range(len(compareList)-1):
        if compareList[i] == compareList[i+1]:
            return True
    return False

if __name__ == '__main__':
    list1 = ['a','a','b','c','d','e','f']
    list2 = ['a','b','c','d']
    list3 = ['ok','ok']

    mainlist = [list1,list2,list3]
    for i in mainlist:
        print has_duplicates(i)
