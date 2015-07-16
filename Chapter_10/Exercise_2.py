__author__ = 'matt'

"""
Use capitalize_all to write a function named capitalize_nested that takes a nested list of strings and returns a new nested list with all strings capitalized.
"""

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

# this function works for nested lists of arbitrary depth
def capitalize_nested(nest_list):
	'''Return a new nested list with all strings capitalized.
	   nest_list -> that takes a nested list of strings.'''
	if isinstance(nest_list, list):
		return [capitalize_nested(s) for s in nest_list]
	else:
		return nest_list.capitalize()

if __name__ == '__main__':
    print "capitalize_all()"
    onelist = ['a','b','c','d']
    print capitalize_all(onelist)
    twolist = [['a','b','c'],['x','Y','Z'],'z','q']
    print capitalize_nested(twolist)
