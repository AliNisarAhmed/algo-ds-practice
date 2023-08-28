def find_kmp(T, P):
    n, m = len(T), len(P)

    if m == 0:
        return 0

    fail = compute_kmp_fail(P)

    j = 0  # index into T
    k = 0  # index into P

    while j < n:
        current = T[j]
        if current == P[k]:
            if k == m - 1:
                return j - m + 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1

    return -1


def compute_kmp_fail(P):
    """Utility that computes and returns KMP 'fail' list"""
    m = len(P)
    fail = [0] * m  # by default, presume overlap of 0 everywhere
    j = 1
    k = 0

    while j < m:
        if P[j] == P[k]:
            fail[j] = k + 1
            j += 1
            k += 1
        elif k > 0:
            # k follows a matching prefix
            k = fail[k - 1]
        else:
            j += 1

    return fail


if __name__ == "__main__":
    T = "abacaabaccabacabaabb"
    P = "abacab"

    # print(find_kmp(T, P))

    T = "aaabaadaabaa"
    P = "aabaaa"

    print(compute_kmp_fail(P))


# R-13.5
# KMP, text=aaabaadaabaa, p=aabaaa
# Answer:
# failure function
#  a a b a a a
#  0 1 0 1 2 2
# aaabaadaabaaa
# aabaaa        after 2 comparisons: fail[0] = 0 + 1; fail[1] = 1 + 1 (fail = 1, 2, 0, 1, 2, 2)
#               at first failure: k = 2 -> k = fail[1] = 1 (fail = 1, 1, 0, 1, 2, 2)
# aaabaadaabaaa
#  aabaaX

