from heap_based_pq import HeapPriorityQueue

# C-9.27


class FIFOQueue:
    def __init__(self):
        self._maxKey = 0
        self._pq = HeapPriorityQueue()

    def enqueue(self, val):
        self._pq.add(self._maxKey, val)
        self._maxKey += 1
        return self

    def dequeue(self):
        _, val = self._pq.remove_min()
        return val


if __name__ == "__main__":
    q = FIFOQueue()
    q.enqueue(1).enqueue(2).enqueue(3)

    print(q.dequeue())
    print(q.dequeue())
    q.enqueue(100)
    q.enqueue(101)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
