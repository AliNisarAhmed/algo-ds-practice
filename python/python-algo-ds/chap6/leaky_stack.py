
# P-6.35
class LeakyStack:
    def __init__(self, maxlen=10):
        self._data = [None] * maxlen
        self._size = 0
        self._front = -1
        self._maxlen = maxlen

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        self._front = (self._front + 1) % self._maxlen
        self._data[self._front] = e
        self._size = min(self._size + 1, self._maxlen)

    def top(self):
        if self.is_empty():
            return None
        return self._data[self._front]

    def pop(self):
        if self.is_empty():
            return None
        res = self._data[self._front]
        self._size = max(self._size - 1, 0)
        self._front = (self._front - 1) % self._maxlen
        return res

    def _atCapacity(self):
        return self._size >= self._maxlen


if __name__ == "__main__":
    s = LeakyStack(3)

    print('----PUSHING NOW----')

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

    print('----POPPING NOW----')

    print(s.pop())
    print('data: ', s._data)
    print('size', s._size)
    print('front', s._front)

    print(s.pop())
    print('data: ', s._data)
    print('size', s._size)
    print('front', s._front)

    print(s.pop())
    print('data: ', s._data)
    print('size', s._size)
    print('front', s._front)

    print(s.pop())
    print('data: ', s._data)
    print('size', s._size)
    print('front', s._front)

    print(s.pop())
    print('data: ', s._data)
    print('size', s._size)
    print('front', s._front)

    print('----PUSHING NOW----')

    s.push(1)
    print('data: ', s._data)
    print('size', s._size)
    print('front', s._front)

    print('----POPPING NOW----')

    print(s.pop())
    print('data: ', s._data)
    print('size', s._size)
    print('front', s._front)
