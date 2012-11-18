__author__ = 'matt'

myDicts = {'matt': 1, 'mary': 1, 'jimmy': 3}

myDicts.setdefault('jimmy',0).append(1)

print myDicts

myDicts.setdefault('joan',0).append(1)

print myDicts

