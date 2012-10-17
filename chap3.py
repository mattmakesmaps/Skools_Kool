"""
Random Edit
Some Dummy Code for Chapter 3
"""
def do_Func(f, val, iter):
    i=0
    while i < iter:
        f(val)
        i+=1

def printer(val):
    """print some stuff"""
    print val

# Create Grid

colCell = '+ - - - - + - - - - +'
rowCell = '|         |         |'

do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)
do_Func(printer, rowCell, 4)
do_Func(printer, colCell, 1)
