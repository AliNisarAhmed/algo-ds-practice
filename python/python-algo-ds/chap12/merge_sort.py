def merge_sort(S):
    """Sort (in-place) elements of Python list S using merge-sort"""
    n = len(S)
    if n < 2:
        return

    mid = n // 2
    S1 = S[0:mid]
    S2 = S[mid:n]

    merge_sort(S1)
    merge_sort(S2)

    merge(S1, S2, S)


def merge(S1, S2, S):
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i += 1
        else:
            S[i + j] = S2[j]
            j += 1


if __name__ == "__main__":
    l = [4, 5, 6, 34, 2, 7, 8, 9, 0]
    merge_sort(l)
    print(l)
