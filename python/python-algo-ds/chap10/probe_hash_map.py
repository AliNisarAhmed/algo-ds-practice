from hash_map_base import HashMapBase


class ProbeHashMap(HashMapBase):
    """Uses open addressing with linear probing"""

    _AVAIL = object()  # sentinel to mark locations of deleted nodes

    def _is_available(self, j):
        """Return True if index j is available in table"""
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL

    def _find_slot(self, j, k):
        """Search for key k in bucket at index j

        Return (success, index) tuple
        if match was found: success = True and index = location
        if no match found: success = False and index = first available slot

        _find_slot continues the search until a truly empty slot is found (i.e. None value)
        but returns the index of the first available slot for an insertion (i.e. _AVAIL)
        """
        first_avail = None
        while True:
            if self._is_available(j):
                if first_avail is None:
                    first_avail = j  # mark this as first available
                if self._table[j] is None:
                    # i.e. not _AVAIL, we must search till an empty slot is reached
                    return (False, first_avail)  # search has failed
            elif k == self._table[j]._key:
                return (True, j)
            j = (j + 1) % len(self._table)  # keep looking (cyclically)

    # R-10.17
    # use Quadratic probing
    def _find_slot_qp(self, j, k):
        first_avail = None
        for i in range(1, 100, 1):
            if self._is_available(j):
                if first_avail is None:
                    first_avail = j
                if self._table[j] is None:
                    return (False, first_avail)
            elif k == self._table[j]._key:
                return (True, j)
            j = (j + i * i) % len(self._table)
        # if we could not find a space, raise error
        raise ValueError("Space not available")

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)  # insert new item
            self._n += 1  # size has increased
        else:
            self._table[s]._value = v  # overwrite existing

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError("Key Error: " + repr(k))
        self._table[s] = ProbeHashMap._AVAIL  # mark as vacated

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key
