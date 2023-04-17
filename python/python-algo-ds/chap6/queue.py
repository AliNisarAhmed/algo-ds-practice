
from collections import deque


class Empty(Exception):
    pass


# R-6.11
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

    def _resize(self, new_capacity):
        old = self._data
        self._data = [None] * new_capacity  # allocate list with new capacity
        # we need this variable otherwise new arrays front would start
        # from the middle
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0  # front has been realigned

    # C-6.29
    def rotate(self):
        """dequeue an element and then enqueue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        # This step is necessay in cases when underlying array has more space
        # than queue size
        # In cases when _size == space, this operation will have no effect
        self._data[(self._front + self._size) %
                   len(self._data)] = self._data[self._front]
        self._front = (self._front + 1) % len(self._data)


def rotate_queue(q: ArrayQueue, count):
    for _ in range(count - 1):
        q.enqueue(q.dequeue())


# R-6.7
# enqueue(5) [5]
# enqueue(3) [5, 3]
# dequeue()                 => 5
# enqueue(2) [3, 2]
# enqueue(8) [3, 2, 8]
# dequeue()                 => 3
# dequeue()                 => 2
# enqueue(9) [8, 9]
# enqueue(1) [8, 9, 1]
# deque()                   => 8
# enqueue(7) [9, 1, 7]
# enqueue(6) [9, 1, 7, 6]
# deque()                   => 9
# deque()                   => 1
# enqueue(4) [7, 6, 4]
# deque()                   => 7
# deque() [4]               => 6


# R-6.8
# 32 enqueue - 15 dequeue + 5 = 22 (current length)

# R-6.9 same operations but queue with max len of 30
# _front moves only when a dequeue is successful
# so answer is 15 - 5(failed) = 10


# R-6.12
# add_first(4)    [4]
# add_last(8)     [4, 8]
# add_last(9)     [4, 8, 9]
# add_first(5)    [5, 4, 8, 9]
# back()                              => 9
# delete_first()  [4, 8, 9]           => 5
# delete_last()   [4, 8]              => 9
# add_last(7)     [4, 8, 7]
# first()                             => 4
# last()                              => 7
# add_last(6)     [4, 8, 7, 6]
# delete_first()  [8, 7, 6]           => 4
# delete_first()  [7, 6]              => 8

# R-6.13 - Convert Deq from 12345678 to 12354678 using Queue

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

# R-6.14 Convert Deq from 12345678 to 12354678 using Stack

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


# C-6.30
# Put 1 even integer in Q
# and rest of 99 integers in R
# chances of Alice's win (she wins with even)
# 0.5 + 0.5 * 49 / 99
# 74.74%


# C-6.31
# yoke can hold 2 cows only, moving at slower cow's speed
# Mazie = 2 min
# Daisy = 4 min
# Crazy = 10 min
# Lazy  = 20 min
# Target = 34 minutes
# 1. Daisy + Mazie = 4
# 2. Daisy back    = 4
# 3. Lazy + Crazy  = 20
# 4. Mazie back    = 2
# 5. Mazie + Daisy = 4
# TOTAL            = 34

# 1. Daisy + Mazie = 4
# 2. Mazie back    = 2
# 3. Lazy + Crazy  = 20
# 4. Daisy back    = 4
# 5. Mazie + Daisy = 4
# TOTAL            = 34
