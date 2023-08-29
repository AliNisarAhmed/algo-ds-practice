def lcs(x, y):
    """Return table such that L[j][k] is
    length of LCS for X[0:j] and Y[0:k]
    """

    n, m = len(x), len(y)

    L = [[0] * (m + 1) for k in range(n + 1)]  # (n + 1) x (m + 1) table

    for j in range(n):
        for k in range(m):
            if x[j] == y[k]:  # align this match
                L[j + 1][k + 1] = L[j][k] + 1
            else:
                L[j + 1][k + 1] = max(L[j][k + 1], L[j + 1][k])

    return L


def lcs_solution(x, y, L):
    """Return the longest common substring of x and y
    given LCS table l
    """

    solution = []

    j, k = len(x), len(y)

    while L[j][k] > 0:
        if x[j - 1] == y[k - 1]:
            solution.append(x[j - 1])
            j -= 1
            k -= 1
        elif L[j - 1][k] >= L[j][k - 1]:
            j -= 1
        else:
            k -= 1

    return ''.join(reversed(solution))


if __name__ == "__main__":
    # x = "AGGTAB"
    # y = "GXTXAYB"
    # L = lcs(x, y)
    X = "skullandbones"
    Y = "lullabybabies"
    L = lcs(X, Y)
    print(L)

    # print(lcs_solution(x, y, L))

# R-13.9
# X = GTTCCTAATA
# Y = CGATAATTGAGA
# GTTTAA is one LCS
# find another
# CTAATA
# and GTAATA

# R-13.10
# X = skullandbones
# Y = lullabybabies
# LCS = ullabes

# def lcs(x, y):
#     """Return table such that L[j][k] is
#     length of LCS for X[0:j] and Y[0:k]
#     """
#
#     n, m = len(x), len(y)
#
#     L = [[0] * (m + 1) for k in range(n + 1)]  # (n + 1) x (m + 1) table
#
#     for j in range(n):
#         for k in range(m):
#             if x[j] == y[k]:  # align this match
#                 L[j + 1][k + 1] = L[j][k] + 1
#             else:
#                 L[j + 1][k + 1] = max(L[j][k + 1], L[j + 1][k])
#
#     return L

# n = = 13
# m = 13
# L = [
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
#     [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#     [0, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]
#     [0, 1, 1, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]
#     [0, 1, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]
#     [0, 1, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]
#     [0, 1, 1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4]
#     [0, 1, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5]
#     [0, 1, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5]
#     [0, 1, 1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 5, 5]
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ]
# j = 0, k = 0, s != l
# j = 0, k = 1, s != u
# j = 0, k = 2, s != l
# j = 0, k = 12, s == s

# j = 1, k = 0, k != l
# j = 1, k = 1, k != u
# j = 1, k = 2, k != l
# j = 1, k = 3, k != l
# j = 1, k = 4 and so on

# j = 2, k = 0, u != l
# j = 2, k = 1, u == u
# j = 2, k = 2, u != l
# j = 2, k = 3, u != l

# j = 3, k = 0, l
# j = 4, k = 0, l
# j = 5, k = 0, a
# j = 6, k = 0, n
# j = 7, k = 0, d
# j = 8, k = 0, b
# j = 11, k = 0, e
