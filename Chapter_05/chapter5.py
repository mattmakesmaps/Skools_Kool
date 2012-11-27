__author__ = 'matt'

def printStuff(s='some default text'):
    """Print a string"""
    print s
    # infinite recursion
    #do_n(printStuff, Chapter_10)

def do_n(f, n=5):
    if n<0:
        return
    f()
    do_n(f, n-1)

def check_fermat(a,b,c,n):
    """check some dead guy's formula"""
    """should be converting all these to ints"""
    if  c**n == a**n + b**n and n>=2:
        print 'Fermat was wrong.'
    else:
        print 'No, that does not work'

def check_fermat_prompt():
    """Execute the check_fermat() function based on user input"""
    a = raw_input('a=')
    b = raw_input('b=')
    c = raw_input('c=')
    n = raw_input('n=')
    check_fermat(int(a),int(b),int(c),int(n))

def getInput(inList, prompt, n):
    """
    Provide an input list, a prompt, and a number of members
    to populate with raw_input() from user
    """
    if n<=0:
        return inList
    else:
        a = raw_input(prompt)
        inList.append(int(a))
        getInput(inList, prompt, n-1)

def is_triangle(edgeList):
    """takes three lengths and reports if they can be a triangle"""
    """
    Thought of using **kws but not appropriate
    since a triangle always has three edges.
    """
    edgeList.sort() # largest number at end

    if edgeList[0] + edgeList[1] >= edgeList[2]:
        print "Yes"
    else:
        print "No"

if __name__ == '__main__':
    # Exercise 5.Chapter_14.4
    print "Begin Exercise 5.Chapter_14 Number 4"
    edgeList = []
    getInput(edgeList, 'Enter Edge Length>>> ', 3)
    is_triangle(edgeList)
