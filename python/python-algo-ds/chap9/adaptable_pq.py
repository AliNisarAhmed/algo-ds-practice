from .heap_based_pq import HeapPriorityQueue


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A location based PQ implemented with a binary heap

    Standard PQs do not suffice in many sitations, e.g.
    - an item in queue may decide to leave early
    - the priority of an item may change

    We use a Locator class to allow the caller/user of the PQ
    to identify elements of PQ for each of update and remove

    Adaptable PQ provide same asymptotic efficiency and space usage
    as a standard PQ
    """

    class Locator(HeapPriorityQueue._Item):
        __slots__ = "_index"

        def __init__(self, k, v, j):
            super().__init__(k, v)
            self._index = j

    def _swap(self, i, j):
        super()._swap(i, j)
        self._data[i]._index = i  # update locator index post-swap
        self._data[j]._index = j  # update locator index (post-swap)

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        token = self.Locator(key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
        """Update the key and value for the entry identified by the Locator loc"""
        j = loc._index

        if not (0 <= j <= len(self) and self._data[j] is loc):
            raise ValueError("invalid locator")

        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc):
        """Remove and return the KV pair identified by Locator loc"""

        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is not loc):
            raise ValueError("invalid locator")

        if j == len(self) - 1:  # i.e. item at last position
            self._data.pop()  # just remove it, no need to bubble up or down
        else:
            self._swap(j, len(self) - 1)  # swap item to the last position
            self._data.pop()
            self._bubble(j)

        return loc._key, loc._value
