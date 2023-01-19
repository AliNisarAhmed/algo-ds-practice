from collections import MapBase


class SortedTableMap(MapBase):
    """Map implementation using a sorted table"""

    def _find_index(self, k, low, high):
        """Return index of the leftmost item with key >= k

        Return high + 1 if no such item qualifies
        i.e. j will be returned such that:
            - all items of slice table [low:j] have key < k
            - all items of slice table [j:high + 1] have key >= k
        """

        if high < low:
            return high + 1
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1)
            else:
                return self._find_index(k, mid + 1, high)  # Answer is right of mid

    def __init__(self):
        self._table = []

    def __len__(self):
        return len(self._table)

    def __getitem(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError("Key Error: " + repr(k))
        return self._table[j]._value

    def __setitem(self, k, v):
        """assign v to key k, override if already present"""
        j = self._find_index(k, 0, len(self._table) - 1)
        if j < len(self._table) and self._table[j]._key == k:
            self._table[j]._value = v
        else:
            self._table.insert(j, self._Item(k, v))

    def __delitem__(self, k):
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError("Key Error: " + repr(k))

    def __iter__(self):
        for item in self._table:
            yield item._key

    def __reversed__(self):
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None

    def find_ge(self, k):
        """Return KV pair with least key >= k"""
        j = self._find_index(k, 0, len(self._table) - 1)  # j's key >= k
        if j < len(self._table):
            return self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_lt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1) # j's key >= k
        if j > 0:
            return (self._table[j - 1]._key, self._table[j-1]._value) # note the use of j - 1
        else:
            return None

    def find_gt(self, k):
        j = self._find_index(k, 0, len(self._table) - 1) # j's key >= k
        if j < len(self._table) and self._table[j]._key == k:
            j += 1 # advanced past match
        if j < len(self._table):
            return (self._table[j]._key, self._table[j]._value)
        else:
            return None

    def find_range(self, start, stop):
        """Iterate all KV pairs such that start <= key <= stop
        
        if start is None, iteration begins withh minimum key of map
        if stop is None, iteration continues thhrough the max key of map
        """

        if start = None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1) # find first result
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1
