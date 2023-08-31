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


# C-13.16
def rfind_brute(T, P):
    """find rightmost index of Pattern p if any"""
    n, m = len(T), len(P)
    for i in range(n - m, -1, -1):
        k = 0
        while k < m and T[i + k] == P[k]:
            k += 1
        if k == m:
            return i
    return -1


# C-13.18
def count_brute(T, P):
    n, m = len(T), len(P)
    count = 0
    for i in range(n - m + 1):
        k = 0
        while k < m and T[i + k] == P[k]:
            k += 1
        if k == m:
            count += 1
            continue
    return count


if __name__ == "__main__":
    T = "abcdabcdxxxabcdxxxx"
    P = "abcd"
    print(rfind_brute(T, P))
    print(count_brute(T, P))

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

# C-13.15
# example of a text with length n and Pattern with length m
# such that brute force is O(nm)
# Make the text and pattern very periodic
# T = aaaaaaaaaaa P = aaaaab
