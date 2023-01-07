import sys

sys.path.append("../chap7")

from positional_list import PositionalList

from priority_queue_base import PriorityQueueBase


class SortedPriorityQueue(PriorityQueueBase):
    """A min-oriented PQ implemented with a sorted Array"""

    def __init__(self):
        self._data = PositionalList()

    def __len__(self):
        return len(self._data)

    def add(self, key, value):
        newest = self._Item(key, value)
        walk = self._data.last()  # walk back looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)
        else:
            self._data.add_after(walk, newest)  # newest goes after walk

    def min(self):
        if self.is_empty():
            raise ValueError("PQ is empty")

        p = self._data.first()
        item = p.element()

        return (item._key, item._value)

    def remove_min(self):
        if self.is_empty():
            raise ValueError("PQ is empty")
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
