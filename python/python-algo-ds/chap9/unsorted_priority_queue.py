from priority_queue_base import PriorityQueueBase
from positional_list import PositionalList
import sys

sys.path.append("../chap7")


class Empty(Exception):
    pass


class UnsortedPriorityQueue(PriorityQueueBase):
    """A min-oriented PQ implemented with an unsorted list"""

    def __init__(self):
        self._data = PositionalList()
        self._min = None

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
        item = self._Item(key, val)
        if self._min is None or self._min > item:
            self._min = item
        self._data.add_last(item)

    # R-9.5
    def min(self):
        item = self._min
        if item is None:
            item = self._find_min().element()
        return (item._key, item._value)

    def remove_min(self):
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)


if __name__ == "__main__":
    pq = UnsortedPriorityQueue()
    print(pq._data)
