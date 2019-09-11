from collections import Counter


def removeDuplicateCharacters(str):
    counter = Counter(str)
    return ''.join([letter for letter in str if counter[letter] == 1])
