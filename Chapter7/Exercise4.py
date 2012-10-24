__author__ = 'matt'

def eval_loop():
    """Take user input and evaluate until user types done"""
    while True:
        exp = raw_input('>>>')
        val = eval(exp)
        print val
        if exp == 'done':
            break
    print "last thing evaluated" + str(val)

if __name__ == '__main__':
    eval_loop()
