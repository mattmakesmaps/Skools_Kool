__author__ = 'matt'
"""
Examples of behaviors of different object types as inputs to loops.
"""

aList = [0,1,2,3,4,5]
aDictionary = {'name':'matt','age':26,'hobby':['gis','bikes']}
aString = 'This Is A String.'
aInt = 87

print 'aList'
for a in aList:
    print a

print 'aDictionary'
for a in aDictionary:
    print a # Iterates over keys, doesn't display values

print 'aString'
for a in aString:
    print a

print 'aInt'
for a in aInt:
    print a
