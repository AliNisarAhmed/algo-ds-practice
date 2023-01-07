import sys

sys.path.append("../chap7")

from positional_list import PositionalList
from priority_queue_base import PriorityQueueBase


class Empty(Exception):
    pass


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented PQ implemented with an unsorted list"""

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def _find_min(self):
        if self.is_empty():
            raise Empty("Priority Queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
                walk = self._data.after(walk)

        return small

    # ---- PUBLIC ----

    def add(self, key, val):
        self._data.add_last(self._Item(key, val))

    def min(self):
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


if __name__ == "__main__":
    pq = UnsortedPriorityQueue()
    print(pq._data)
