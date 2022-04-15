import ctypes


class DynamicArray:

    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)

    def _make_array(c):
        """ return new array with capacity c"""
        return (c * ctypes.py_object)()

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        if k > self._n or k < -1 * self._n:
            raise IndexError('invalid index')
        if k < 0:
            return self._A[self._n + k]
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c):
        B = self._make_array(c)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = c

    def insert(self, k, val):
        if self._n == self._capacity:
            # resize while shifting
            new_cap = 2 * self._capacity
            B = self._make_array(new_cap)
            for j in range(k):
                B[j] = A[j]
            for j in range(k + 1, self._n):
                B[j] = self._A[j]
            self._A = B
            self._capacity = new_cap
        self._A = val
        self._n += 1

    def stats():
        print('Length: ', self._n)
        print('Cap: ', self._capacity)
        print('Underlying array', self._A)

l = DynamicArray()
l.insert(1)
l.stats()
l.insert(2)
l.stats()
l.insert(3)
l.stats()
