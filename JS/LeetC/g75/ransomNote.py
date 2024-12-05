from collections import Counter


def canConstruct(ransomNote, magazine):

    if len(ransomNote) > len(magazine):
        return False

    letters = Counter(magazine)

    for c in ransomNote:
        if not letters[c] or letters[c] <= 0:
            return False

    letters[c] = letters[c] - 1

    return True
