__author__ = 'matt'

def is_reverse(word1, word2):
    if len(word1) != len(word2):
        return False

    i = 0
    j = len(word2) - 1

    while i < len(word1):
        if word1[i] != word2[j]:
            return False
        i += 1
        j -= 1

    return True

if __name__ == '__main__':
    print is_reverse('pots', 'stop')
