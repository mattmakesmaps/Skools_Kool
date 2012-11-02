__author__ = 'matt'

"""
Use capitalize_all to write a function named capitalize_nested that takes a nested list of strings and returns a new nested list with all strings capitalized.
"""

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(t):
    res = []
    for innerlist in t:
        if isinstance(innerlist, list):
            newList = []
            for element in innerlist:
                newList.append(element.capitalize())
            res.append(newList)
        else:
            res.append(innerlist.capitalize())
    return res

if __name__ == '__main__':
    print "capitalize_all()"
    onelist = ['a','b','c','d']
    print capitalize_all(onelist)
    twolist = [['a','b','c'],['x','Y','Z'],'z','q']
    print capitalize_nested(twolist)
