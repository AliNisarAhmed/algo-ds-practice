class Empty(Exception):
    pass


class Full(Exception):
    pass


class ArrayStack:

    def __init__(self, maxlen=None):
        self._data = [] if maxlen is None else [None] * maxlen
        self._size = 0
        self._maxlen = maxlen

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        if self._atCapacity():
            raise Full('Stack is full')
        if self._maxlen is None:
            self._data.append(e)
        else:
            self._data[self._size] = e
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        self._size -= 1
        return self._data.pop()

    def _atCapacity(self):
        if not self._maxlen:
            return False
        return self._size >= self._maxlen


def remove_all_rec(S):
    if S.is_empty():
        return
    S.pop()
    remove_all_rec(S)


def reverse_list(ls):
    S = ArrayStack()
    for i in range(len(ls)):
        S.push(ls[i])
    for j in range(len(ls)):
        ls[j] = S.pop()
    return ls


def transfer(S: ArrayStack, T: ArrayStack):
    """ Transfer all elements of S to T"""
    while not S.is_empty():
        e = S.pop()
        T.push(e)
