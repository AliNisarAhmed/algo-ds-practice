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
