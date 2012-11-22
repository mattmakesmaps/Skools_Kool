__author__ = 'matt'

class classOne(object):
    """
    For this class, when you create an instance, the value given for argument x
    is automatically overwritten. You can however, re assign the instance variable
    later one. Can you re assign the class variable as well?
    """
    def __str__(self):
        return 'this is an __str__ my name is matt'

    def __init__(self, x, y):
        self.x = 202
        self.y = y

class classTwo(object):
    def __str__(self):
        return 'this is an __str__ my name is matt'

    def __init__(self, x, y):
        self.x = 202
        self.y = y

if __name__ == '__main__':
    intOneClassOne = classOne(10,11)
    print str(intOneClassOne)
    print intOneClassOne.x
    print intOneClassOne.y

    intTwoClassOne = classOne(14,11)
    print str(intOneClassOne)
    intTwoClassOne.x = 10
    print intTwoClassOne.x
    print intTwoClassOne.y

    classOne.y = 33
    print classOne.y

    intThreeClassOne = classOne(14,11)
    print str(intOneClassOne)
    print intThreeClassOne.x
    print intThreeClassOne.y

    intFourClassOne = classOne(14,11)
    print str(intOneClassOne)
    print intFourClassOne.x
    print intFourClassOne.y

