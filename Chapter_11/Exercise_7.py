__author__ = 'matt'
"""
Memoize the Ackermann function from Exercise 6.5 and see if memoization makes it possible to evaluate the function with bigger arguments. Hint: no. Solution: http://thinkpython.com/code/ackermann_memo.py.
"""

known = dict()

def ackermann_book(m, n):
    # TODO: solution uses try/execpt block
    """Computes the Ackermann function A(m, n)

    See http://en.wikipedia.org/wiki/Ackermann_function

    n, m: non-negative integers
    """
    if (m,n) in known:
        return known[(m,n)]

    if m == 0:
        res = n+1
        known[(m,n)] = res
        return res
    if n == 0:
        res = ackermann_book(m-1, 1)
        known[(m,n)] = res
        return res

    res = ackermann_book(m-1, ackermann_book(m, n-1))
    known[(m,n)] = res
    return res

if __name__ == '__main__':
    print ackermann_book(4,2)
