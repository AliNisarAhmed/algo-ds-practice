import sys


def matrix_chain(d):
    """d is a list of n + 1 numbers
    such that the size of kth matrix is d[k] x d[k + 1]

    Return an n x n table such that N[i][j] represents the min number
    of multiplications needed to compute the product of Ai through Aj inclusive
    """

    n = len(d) - 1  # number of matrices
    N = [[0] * n for i in range(n)]  # initialize n x n result to 0

    for b in range(1, n):  # number of products in subchain
        for i in range(n - b):  # start of subchain
            j = i + b  # end of subchain
            N[i][j] = min(N[i][k] + N[k + 1][j] + d[i] * d[k + 1] * d[j + 1]
                          for k in range(i, j))
    return N


dp = [[-1 for i in range(100)] for j in range(100)]


def matrix_chain_memoised(p, i, j):
    if i == j:
        return 0

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = sys.maxsize

    for k in range(i, j):
        dp[i][j] = min(dp[i][j],
                       matrix_chain_memoised(p, i, k) +
                       matrix_chain_memoised(p, k + 1, j) +
                       p[i - 1] * p[k] * p[j])

    return dp[i][j]


def matrix_chain_order(p, n):
    i = 1
    j = n - 1
    return matrix_chain_memoised(p, i, j)


if __name__ == "__main__":
    arr = [1, 2, 3, 4]
    print(matrix_chain(arr))

    print(matrix_chain_order(arr, len(arr)))
