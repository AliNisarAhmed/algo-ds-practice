from heap_based_pq import HeapPriorityQueue


# C-9.26
class StackUsingPQ:
    def __init__(self):
        self._index = 0
        self._pq = HeapPriorityQueue()

    def push(self, value):
        self._pq.add(self._index, value)
        self._index -= 1
        return self

    def pop(self):
        (_, value) = self._pq.remove_min()
        self._index += 1
        return value

    def top(self):
        (_, value) = self._pq.min()
        return value


if __name__ == "__main__":
    s = StackUsingPQ()
    s.push(1).push(2).push(3)

    print(s.pop())

    s.push(4)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    s.push(100)
    print(s.pop())
