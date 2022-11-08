from stack import Empty


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
        if 0 < self._size < len(self.data) // 4:
            self._resize(len(self.data) // 2)

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
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0  # front has been realigned
