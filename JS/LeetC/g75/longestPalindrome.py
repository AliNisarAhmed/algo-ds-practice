def longestPalindrome(s):
    sset = set()

    count = 0
    for letter in s:
        if letter in sset:
            count += 2
            sset.remove(letter)
        else:
            sset.add(letter)

    return count + 1 if len(sset) > 0 else count
