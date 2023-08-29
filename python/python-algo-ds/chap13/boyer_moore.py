def find_boyer_moore(T, P):
    n, m = len(T), len(P)

    if m == 0:
        return 0

    last = {}

    for k in range(m):
        # last occurence of a character in P
        last[P[k]] = k

    # align end of patter at index m - 1 of text
    i = m - 1  # an index into T
    k = m - 1  # an index into P

    while i < n:
        current = T[i]
        if current == P[k]:
            if k == 0:
                # found the match
                return i
            else:
                # examine previous character of both T and P
                i -= 1
                k -= 1
        else:
            j = last.get(current, -1)
            i += m - min(k, j + 1)
            k = m - 1

    return -1


if __name__ == "__main__":
    T = "a quick brown fox jumped over a lazy fox"
    P = "over"

    # print(find_boyer_moore(T, P))

    T = "aaabaadaabaaa"
    P = "aabaaa"
    print(find_boyer_moore(T, P))


# R-13.4
# Boyer moore text=aaabaadaabaaa, pattern=aabaaa
# Answer
# last = {b: 2, a: 5}
# aaabaadaabaaa
#    Xaa
# aaabaadaabaaa
#  aabaaX       -> i + m - (j + 1) -> 3 + 6 - (2 + 1) -> 6 -> index of d
# aaabaadaabaaa
#        aabaaa -> Answer = 7


# R-13.6
# compute last function for
# s = "the quick brown fox jumped over a lazy cat"
# last = {
# t: 39,
# h: 1,
# e: 28,
# q: 4,
# u: 21,
# i: 6,
# c: 36,
# k: 8,
# b: 10,
# r: 29,
# o: 27,
# w: 13,
# n: 14,
# f: 16
# x: 18,
# j: 20,
# m: 22,
# p: 23,
# d: 25,
# v: 27,
# a: 37,
# l: 32,
# z: 33,
# y: 34,
# ' ': 35,
# }
