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

    print(find_boyer_moore(T, P))
