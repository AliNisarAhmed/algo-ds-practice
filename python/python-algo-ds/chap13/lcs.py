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
    current = L[j][k]
    while current > 0:
        if x[j - 1] == y[k - 1]:
            solution.append(x[j - 1])
            j -= 1
            k -= 1
        elif L[j - 1][k] >= L[j][k - 1]:
            j -= 1
        else:
            k -= 1
        current = L[j][k]

    return ''.join(reversed(solution))


if __name__ == "__main__":
    X = "AGGTAB"
    Y = "GXTXAYB"
    # L = lcs(x, y)
    # X = "skullandbones"
    # Y = "lullabybabies"
    L = lcs(X, Y)
    print(L)

    print(lcs_solution(X, Y, L))

# R-13.9
# X = GTTCCTAATA
# Y = CGATAATTGAGA
# GTTTAA is one LCS
# find another
# CTAATA
# and GTAATA

# R-13.10
# X = AGGTAB
# Y = GXTXAYB
#
# def lcs(x, y):
#     """Return table such that L[j][k] is
#     length of LCS for X[0:j] and Y[0:k]
#     """
#     n, m = len(x), len(y)
#     L = [[0] * (m + 1) for k in range(n + 1)]  # (n + 1) x (m + 1) table
#     for j in range(n):
#         for k in range(m):
#             if x[j] == y[k]:  # align this match
#                 L[j + 1][k + 1] = L[j][k] + 1
#             else:
#                 L[j + 1][k + 1] = max(L[j][k + 1], L[j + 1][k])
#     return L
#
# n = 6, m = 7
# L = [
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1, 1, 1],
#     [0, 1, 1, 1, 1, 1, 1, 1],
#     [0, 1, 1, 2, 2, 2, 2, 2],
#     [0, 1, 1, 2, 2, 3, 3, 3],
#     [0, 1, 1, 2, 2, 3, 3, 4],
#         ]
# j = 0 -> 5, k = 0 -> 6
# j = 3, k = 0, T-G
# j = 2, k = 0, G-G
#
# j = 1, k = 4, G-A
# j = 1, k = 3, G-X
# j = 1, k = 2, G-T
# j = 1, k = 1, G-X
# j = 1, k = 0, G-G

# j = 0, k = 5, A-Y
# j = 0, k = 4, A-A
# j = 0, k = 3, A-X
# j = 0, k = 2, A-T
# j = 0, k = 0, A-G
# j = 0, k = 1, A-X
