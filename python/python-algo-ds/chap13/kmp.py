def find_kmp(T, P):
    n, m = len(T), len(P)

    if m == 0:
        return 0

    fail = compute_kmp_fail(P)

    j = 0  # index into T
    k = 0  # index into P

    while j < n:
        current = T[j]
        pattern_current = P[k]
        if current == pattern_current:
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


# C-13.18
def rfind_kmp(T, P):
    n, m = len(T), len(P)
    if m == 0:
        return 0

    fail = rcompute_kmp_fail(P)

    j = n - 1
    k = m - 1

    while j >= 0:
        text_current = T[j]
        pattern_current = P[k]
        if text_current == pattern_current:
            if k <= 0:
                return j
            j -= 1
            k -= 1
        elif k > 0 and k < m - 1:
            k = m - fail[k + 1] - 1
        else:
            j -= 1
    return -1


def rcompute_kmp_fail(P):
    m = len(P)
    fail = [0] * m
    front = m - 2  # j
    back = m - 1  # k
    match = 0

    while front >= 0:
        if P[front] == P[back]:
            match += 1
            fail[front] = match
            front -= 1
            back -= 1
        elif back < m - 1:
            back = fail[back + 1]
            match = back
        else:
            front -= 1
    return fail


# C-13.21
def count_kmp(T, P):
    count = 0
    n, m = len(T), len(P)
    if m == 0:
        return 0

    fail = compute_kmp_fail(P)

    j = 0
    k = 0

    while j < n:
        if T[j] == P[k]:
            if k == m - 1:
                count += 1
                j += 1
                k = 0
                continue
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
        else:
            j += 1
    return count


# C-13.23
def longest_prefix_substring(T, P):
    n, m = len(T), len(P)
    maxIndex = 0
    maxLen = 0
    currentLen = 0

    fail = compute_kmp_fail(P)

    j = 0
    k = 0

    while j < n:
        if T[j] == P[k]:
            currentLen += 1
            j += 1
            k += 1
        elif k > 0:
            k = fail[k - 1]
            if currentLen > maxLen:
                maxLen = currentLen
                maxIndex = j - k
            currentLen = 0
        else:
            j += 1
    return maxIndex, maxLen


if __name__ == "__main__":
    T = "abacaabaccabacabaabb"
    P = "abacab"

    # print(find_kmp(T, P))

    T = "aaabaadaabaaa"
    # P = "aabaaa"

    P = "abxyz"

    # print(find_kmp(T, P))

    s = "cgtacgttcgtac"

    # print(compute_kmp_fail(s))
    # print(compute_kmp_fail("aaacaaaa"))
    # print(rcompute_kmp_fail("aaacaaaa"))

    # T = "abcaabbd1234abba12345abba"
    T = "xlkjljfgijefnwligwlgi"
    P = "abba"

    print(rcompute_kmp_fail(P))
    print(rfind_kmp(T, P))

    T = "abcdabcdabcdabcx"
    P = "abcd"
    print(count_kmp(T, P))

    T = "12345678"
    P = "123xae"
    print(longest_prefix_substring(T, P))


# R-13.5
# KMP, text=aaabaadaabaa, p=aabaaa
# Answer:
# failure function
#  a a b a a a
#  0 1 0 1 2 2
# aaabaadaabaaa
# aabaaa        after 2 comparisons: fail[0] = 0 + 1; fail[1] = 1 + 1 (fail = 1, 2, 0, 1, 2, 2)
#               at first failure: k = 2 -> k = fail[1] = 1 (fail = 1, 1, 0, 1, 2, 2)
# aa[a]baadaabaaa j = 2
# aa[b]aaa k = 2
#
# aa[a]baadaabaaa j= 2
# a[a]baaa k = 1

# aaabaa[d]aabaaa   j = 6
# aabaa[a]          k = 5
# k = fail[4] = 2

# aabaa[d]aabaaa    j = 6
# aa[b]aaa          k = 2
# k = fail[1] = 1

# aabaa[d]aabaaa    j = 6
# a[a]baaa          k = 1
# k = fail[0] = 0

# aabaa[d]aabaaa    j = 6
# [a]abaaa          k = 0
# k = 0, j =7

# aabaad[a]abaaa
# [a]abaaa      full match


# R-13.7
# compute failure func for
# s = "cgtacgttcgtac"
# fail = [0, 0, 0, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5]
