"""
Some Dummy Code for Chapter 3
"""
def do_Func(f, val, iter):
    i=0
    while i < iter:
        f(val)
        i=i+1

def printer(val):
    print val

do_Func(printer, 'some value', 5)

# Create Grid

colCell = '+ - - - - + - - - - +'
rowCell = '|         |         |'

do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)
