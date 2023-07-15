from map_base import MapBase


# R-10.5
class UnsortedTableMap(MapBase):
    """Map implementation using an unordered list"""

    def __init__(self):
        self._table = []

    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError("Key Error: " + repr(k))

    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError("Key Error: " + repr(k))

    def __len__(self):
        return len(self._table)

    def __iter__(self):
        for item in self._table:
            yield item._key

    # R-10.3 implement items ensuring it is O(n)
    def items(self):
        for item in self._table:
            yield item._key, item._value

    # C-10.28
    def setdefault(self, key, value):
        for item in self._table:
            if item._key == key:
                item._value = value
                return
        self._table.append(self._Item(key, value))

    # R-10.4 what is the worst case time for inserting n kv pairs
    # into UnsortedTableMap
    # Answer: O(n^2)
    # O(1) for first key
    # O(2) for second key and so on
    # for each key, we need to traverse the whole list in order
    # to ensure it is not already present
    # we cannot simply append it at the end

    # R-10.6 which of the hash table collision-handling schemes could tolerate
    # a load factor above 1 and which could not?
    # Open addressing cannot, since it uses the same array supporting hash table
    # Separate chaining can, since it uses a different array for each key position


if __name__ == "__main__":
    m = UnsortedTableMap()
    m[1] = "A"
    m[2] = "B"
    m[3] = "Azlan"

    for (k, v) in m.items():
        print("Key: " + repr(k))
        print("Value: " + repr(v))
        print("----")
