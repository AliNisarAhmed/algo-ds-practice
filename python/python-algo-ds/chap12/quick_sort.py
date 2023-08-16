from ..chap7.linkedQueue import LinkedQueue


def quick_sort(S: LinkedQueue):
    n = len(S)
    if n < 2:
        return

    p = S.first()  # using first as arbitrary pivot
    L = LinkedQueue()
    E = LinkedQueue()
    G = LinkedQueue()

    while not S.is_empty():
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:
            E.enqueue(S.dequeue())

    quick_sort(L)
    quick_sort(E)

    while not L.is_empty():
        S.enqueue(L.dequeue())

    while not E.is_empty():
        S.enqueue(E.dequeue())

    while not G.is_empty():
        S.enqueue(G.dequeue())
