__author__ = 'matt'

"""
Write a function called nested_sum that takes a nested list of integers and add up
the elements from all of the nested lists.
"""

def nested_sum(listin):
    """Given a nested list, return the sum of all elements"""
    total = 0
    for innerlist in listin:
        for element in innerlist:
            total += element
    return total

def nested_sumConditional(listin):
    """Use conditional to return sum of all elements"""
    total = 0
    for innerlist in listin:
        if isinstance(innerlist, list):
            for element in innerlist:
                total += element
        else:
            total += innerlist
    return total

def nested_sumWhileRecursive(listin, total=0):
    """Use while loop and recursion to return sum of all elements"""
    counter = len(listin)
    while counter > 0:
        if isinstance(listin[0], list):
            for element in listin[0]:
                total += element
        else:
            total += listin[0]
        del listin[0]
        return nested_sumWhileRecursive(listin, total)
    return total

if __name__ == '__main__':
    print "Run One."
    oneList = [[3,3],[3,3],[3,3]]
    print nested_sum(oneList)
    print "Run Two."
    twoList = [[3,3],[3,3],[3,3],3,3]
    print nested_sumConditional(twoList)
    print "Run Three."
    threeList = [[3,3],[3,3],[3,3],3,3]
    print nested_sumWhileRecursive(threeList)
