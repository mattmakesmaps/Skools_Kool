__author__ = 'matt'

"""
Return new list with unique elements only.
"""

def remove_duplicates(inList):
    """Return new list with unique elements only. In Future, can use set"""
    compareList = inList[:]
    compareList.sort()
    # Need to create second list that can have elements deleted from
    # Delete elements from compareList will create a shorter number of indexes
    # causing the loop the fail
    finalList = compareList[:]

    for i in range(len(compareList)-1):
        if compareList[i] == compareList[i+1]:
            del(finalList[i])
    return finalList

if __name__ == '__main__':
    list1 = ['a','a','b','c','d','e','f']
    list2 = ['a','b','c','d']
    list3 = ['ok','ok']

    mainlist = [list1,list2,list3]
    for i in mainlist:
        print remove_duplicates(i)
