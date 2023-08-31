import random


def quick_select(S, k):
    """Return the kth smallest element of list S, for k from 1 to len(S)"""
    if len(S) == 1:
        return S[0]

    pivot = random.choice(S)
    L = [x for x in S if x < pivot]
    E = [x for x in S if x == pivot]
    G = [x for x in S if x > pivot]

    if k <= len(L):
        return quick_select(L, k)  # smallest lies in L
    elif k <= len(L) + len(E):
        return pivot  # kth smallest == pivot
    else:
        j = k - len(L) - len(E)  # new selection parameter
        return quick_select(G, j)


if __name__ == "__main__":
    l = [4, 3, 5, 6, 8, 7, 1, 2, 9]
    print(quick_select(l, 4))
