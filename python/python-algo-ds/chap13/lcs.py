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
    x = "AGGTAB"
    y = "GXTXAYB"
    L = lcs(x, y)
    print(L)

    print(lcs_solution(x, y, L))
