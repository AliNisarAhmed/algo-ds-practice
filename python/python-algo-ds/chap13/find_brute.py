def find_brute(T, P):
    """Return the lowest index of T at which substring P begins (or else -1)"""
    n, m = len(T), len(P)
    for i in range(n - m + 1):
        # don't search for strings smaller than m at the end
        k = 0
        while k < m and T[i + k] == P[k]:
            k += 1
        if k == m:
            # we matched the full substring
            return i

    return -1


# R-13.1
# List prefixes of String = "aaabbaaa" that are also suffixes of
# Answer = 4
# a -> a
# aa -> aa
# aaa -> aaa
# "" -> "" (empty string)


# R-13.2
# what is the longest proper prefix of string below that is also a suffix
# s = "cgtacgttcgtacg"
# Answer
# cgtacg

# R-13.3
# brute force text="aaaabaadaabaaa", pattern = "aabaaa"
# [a]aaabaadaabaa
# aaX
# a[a]aabaadaabaaa
#   aaX
# aa[a]abaadaabaaa
#    aabaaX
# and so on, till it matches at aaaabaad[a]abaaa
