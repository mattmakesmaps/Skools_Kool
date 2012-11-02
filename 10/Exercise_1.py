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
        if isinstance(listin, list):
            for element in innerlist:
                total += element
        else:
            total += innerlist
    return total


if __name__ == '__main__':
    print "Run One."
    oneList = [[3,3],[3,3],[3,3]]
    print nested_sum(oneList)
    print "Run Two."
    twoList = [[3,3],[3,3],[3,3],3,3]
    print nested_sumConditional(twoList)
