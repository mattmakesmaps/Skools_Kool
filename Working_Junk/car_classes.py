__author__ = 'matt'

class Tire(object):
    """tire for car"""
    def __init__(self, psi=32, tread='all weather'):
        self.psi = psi
        self.tread = tread

class Car(object):
    """a car class"""
    def __init__(self, numtires):
        self.tires = [] # An attribute to hold all Tire instances
        for i in range(numtires):
            self.tires.append(Tire())
        self.make = 'ford'
        self.model = 'pinto'
        self.year = 1996

if __name__ == '__main__':
    myCar = Car(4)
    print myCar.make
    print myCar.tires[0].psi # access each Tire() through its tires attribute index.
    myCar.tires[0].psi = 60
    print myCar.tires[0].psi
    print myCar.tires[1].psi
