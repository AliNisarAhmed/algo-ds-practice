# from positional_list import PositionalList
from priority_queue_base import PriorityQueueBase

# import sys
#
# sys.path.append("../chap7")


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


# C-9.29
class SortedPQWithList(PriorityQueueBase):
    """
    A min oriented PQ implemented with a python list

    To ensure remove_min remains O(1), we store the items in descending order
    """

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self) == 0

    def add(self, key, value):
        newest = self._Item(key, value)
        index = -1
        for i in range(len(self._data)):
            if self._data[i] < newest:
                index = i
                break
        if index == -1:
            self._data.append(newest)
        else:
            self._data.insert(index, newest)

    def min(self):
        if self.is_empty():
            raise ValueError("PQ is empty")

        item = self._data[len(self._data) - 1]
        return item._key, item._value

    def remove_min(self):
        if self.is_empty():
            raise ValueError("PQ is empty")

        item = self._data.pop()
        return item._key, item._value

    def to_list(self):
        return list(map(lambda x: (x._key, x._value), self._data))


if __name__ == "__main__":
    pq = SortedPQWithList()
    pq.add(0, "a")
    pq.add(1, "b")
    pq.add(2, "c")
    print(pq.to_list())
    pq.remove_min()
    print(pq.to_list())
    pq.remove_min()
    pq.add(0, "d")
    print(pq.to_list())
