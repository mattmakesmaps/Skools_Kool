__author__ = 'matt'

"""
Two words are anagrams if you can rearrange the letters from one to spell the other. Write a function called is_anagram that takes two strings and returns True if they are anagrams.
"""

def is_anagram(string1, string2):
    """return True if strings are anagrams of each other"""
    list1 = list(string1)
    list2 = list(string2)
    list1.sort()
    list2.sort()
    return list1 == list2

if __name__ == '__main__':
    string1='abcdef'
    string2='fedcba'
    print is_anagram(string1, string2)
    string3='ubuntu'
    string4='whatthe'
    print is_anagram(string3, string4)