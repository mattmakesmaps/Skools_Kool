def recursionTest(n):
    if n<=0:
        print 'blastoff!'
    else:
        print n
        recursionTest(n-1)

if __name__ == '__main__':
    recursionTest(10)