
# P-6.35
class LeakyStack:
    def __init__(self, maxlen=10):
        self._data = [None] * maxlen
        self._size = 0
        self._front = 0
        self._maxlen = maxlen

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        if self._atCapacity():
            last = (self._front + 1) % self._maxlen
            self._data[last] = e
            self._front = last
        else:
            self._data[self._front] = e
            self._front = (self._front + 1) % self._maxlen
            self._size += 1

    def top(self):
        if self.is_empty():
            # TODO
            pass
        return self._data[self._front]

    def pop(self):
        if self.is_empty():
            # TODO
            pass
        prev = (self._front - 1) % self._maxlen
        res = self._data[prev]
        self._data[prev] = None
        self._front = prev
        self._size -= 1
        return res

    def _atCapacity(self):
        return self._size >= self._maxlen


if __name__ == "__main__":
    s = LeakyStack(3)
    # s.push(1)
    # s.push(2)
    # print('data: ', s._data)
    # print('size', s._size)
    # print('front', s._front)
    # print('pop: ', s.pop())
    # print('pop: ', s.pop())
    # print('data: ', s._data)
    # print('size', s._size)
    # print('front', s._front)

    s.push(1)
    print('data: ', s._data)
    print('size', s._size)
    print('front', s._front)
    s.push(2)
    print('data: ', s._data)
    print('size', s._size)
    print('front', s._front)
    s.push(3)
    print('data: ', s._data)
    print('size', s._size)
    print('front', s._front)
    s.push(4)
    print('data: ', s._data)
    print('size', s._size)
    print('front', s._front)
