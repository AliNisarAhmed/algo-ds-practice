
from collections import deque


class Empty(Exception):
    pass


class DeckQueue:

    def __init__(self):
        self._data = deque()

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[0]

    def dequeue(self):
        return self._data.popleft()

    def enqueue(self, x):
        return self._data.append(x)


class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        # divide by len(self._data) and not DEFAULT_CAPACITY because underlying
        # array can be resized

        # move front 1 step to right, also taking care of wrapping using %
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1

        # shrink the underlying array if the size is less than quarter of the array
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)

        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))

        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def _resize(self, cap):
        old = self._data
        self._data = [None] * cap  # allocate list with new capacity
        # we need this variable otherwise new arrays front would start
        # from the middle
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0  # front has been realigned


def rotate_queue(q: ArrayQueue, count):
    for _ in range(count - 1):
        q.enqueue(q.dequeue())

# 6-13 - Convert Deq from 12345678 to 12354678 using Queue

# D [1, 2, 3, 4, 5, 6, 7, 8]
# Q - front [] back

# 5 x delete_first
# D [6, 7, 8]
# Q [1, 2, 3, 4, 5]

# 3 x dequeue and 3 x add_last
# D [6, 7, 8, 1, 2, 3]
# Q [4, 5]

# 2 x dequeue and 2 X add_first
# D [ 5, 4, 6, 7, 8, 1, 2, 3]
# Q []

# 3 x delete_last
# D [5, 4, 6, 7, 8]
# Q [3, 2, 1]

# 3 x dequeue and 3 x add_first
# D [1, 2, 3, 5, 4, 6, 7, 8]
# Q [] - QED

# 6-14 Convert Deq from 12345678 to 12354678 using Stack

# D [1, 2, 3, 4, 5, 6, 7, 8]
# S [] top

# 4 x delete_first
# D [5, 6, 7, 8]
# S [1, 2, 3, 4]

# 1 x stack pop and 1 x add_last
# D [5, 6, 7, 8, 4]
# S [1, 2, 3]

# 1 x delete_first
# D [6, 7, 8, 4]
# S [1, 2, 3, 5]

# 1 x delete_last
# D [6, 7, 8]
# S [1, 2, 3, 5, 4]

# 5 x add_first
# D [1, 2, 3, 5, 4, 6, 7, 8]
# S [] - QED
