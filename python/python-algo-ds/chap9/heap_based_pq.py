"""
Heap Data Structure

A heap is a BT that stores a collection of items and satisfies two additional properties:
    1. Relational-property: Heap-Order property
        - in a heap T, for every position p other than root,
          the key stored at p is >= key stored at p's parent
        - The minimum is always stored at the root
    2. Structural-property: Complete BT property
        - A heap T with height h is complete BT if all internal levels (0, 1, 2... h - 1)
          have the max numbers of nodes possible, and at the leaf level (level h), all the nodes
          reside in the leftmost possible positions at that level

The height of a heap storing n entries is given by
    - h = floor(log n)
"""
from priority_queue_base import PriorityQueueBase


class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented PQ implemented with a binary heap"""

    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        """Determine smallest child and swap with it, recurse"""
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(small_child, j)
                self._downheap(small_child)

    # ---- PUBLIC ------

    def __init__(self, contents=()):
        """
        Create a new PQ

        By default, the queue will be empty, if contents is given,
        it should be as an iterable sequence of (k,v) tuples
        specifying the initial contents
        """
        self._data = [self._Item(k, v) for k, v in contents]
        if len(self._data) > 1:
            # if contents is given, ensure they follow heap properties
            self._heapify()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        """Add a KV pair to the end of PQ and upheap"""
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)

    def min(self):
        if self.is_empty():
            raise ValueError("PQ is empty")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError("PQ is empty")
        item = self._data[0]
        self._data[0] = self._data.pop()
        self._downheap(0)
        return item._key, item._value

    def _heapify(self):
        """Bottom up heap construction
        This runs in O(n) time, as opposed to multiple calls to add operation
        which will take O(nlogn) in the worst case
        """
        start = self._parent(len(self) - 1)  # start at parent of last leaf
        for j in range(start, -1, -1):  # going to and including the root
            self._downheap(j)
