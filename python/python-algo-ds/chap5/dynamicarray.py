import ctypes
import sys

data = []


def showUnderlyingSize(n):
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        print('Length {0:3d}; Size in bytes: {1:4d}'.format(a, b))
        data.append(None)


# R-5.2
def showUnderlyingSize2(n):
    size_old = 0
    for k in range(n):
        a = len(data)
        b = sys.getsizeof(data)
        if b != size_old:
            print('Length {0:3d}; Size in bytes: {1:4d}'.format(a, b))
            size_old = b
        data.append(None)


showUnderlyingSize2(26)


# -----------

# R-5.3
def array_grow_shrink(n, lower_limit=0.2):
    data = []
    size_old = 0
    current_limit = 10
    for i in range(n):
        if i == current_limit:
            while len(data) > current_limit * lower_limit:
                data.pop()
                size = sys.getsizeof(data)
                print(len(data), size, end='\t\t')
                if size < size_old:
                    print('size decreased from: ', size_old, size)
                else:
                    print("")
                size_old = size
            current_limit *= 10
        data.append(None)


array_grow_shrink(1000)

# -----------


class DynamicArray:
    def __init__(self):
        self._n = 0
        self._capacity = 1
        self._A = self._make_array(self._capacity)  # low level unerlying array

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        # if not 0 <= k < self._n:
        if not k < self._n:
            raise IndexError('invalid index')
        return self._A[k]

    def append(self, obj):
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, new_capacity):
        """Resize internal array to capacity c"""
        B = self._make_array(new_capacity)
        for k in range(self._n):
            B[k] = self._A[k]
        self._A = B
        self._capacity = new_capacity

    def _make_array(self, c):
        return (ctypes.py_object*c)()

    def insert(self, k, value):
        """Insert value at index k, shifting subsequent values rightward"""
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        for j in range(self._n, k, -1):
            self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1
        print(self._n)

    # R-5.6
    def insert2(self, k, value):
        if self._n == self._capacity:
            B = self._make_array(2 * self._capacity)
            for j in range(self._n + 1, k, -1):
                B[j] = self._A[j - 1]
            self._capacity = 2 * self._capacity
        else:
            for j in range(self._n + 1, k, -1):
                self._A[j] = self._A[j - 1]
        self._A[k] = value
        self._n += 1

    def remove(self, value):
        for k in range(self._n):
            if self._A[k] == value:
                for j in range(k, self._n - 1):
                    self._A[j] = self._A[j + 1]
                self._A[self._n - 1] = None
                self._n -= 1
        raise ValueError('value not found')
