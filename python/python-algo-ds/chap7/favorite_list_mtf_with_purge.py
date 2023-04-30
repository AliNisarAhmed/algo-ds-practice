from positional_list import PositionalList


# C-7.40
class FavoritesListMTFWithPurge():
    class _Item:
        __slots__ = '_value', '_count', '_accessed_at'

        def __init__(self, e):
            self._value = e
            self._count = 0
            self._accessed_at = 0

    def __init__(self, purge_point=10):
        self._data = PositionalList()
        self._access_count = 0
        self._purge_point = purge_point

    def _find_position(self, e):
        """Search for element e and returns its Position"""
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, p):
        """
        Move item at Position p earlier in the list based on access count

        Very similar to how insertion sort item is bubbled up"""
        if p != self._data.first():
            # delete/reinsert at first pos
            self._data.add_first(self._data.delete(p))

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count"""

        p = self._find_position(e)

        if p is None:
            p = self._data.add_last(self._Item(e))

        self._access_count += 1
        p.element()._count += 1
        p._accessed_at = self._access_count
        self._move_up(p)
        self.purge()

    def purge(self):
        last = self._data.last()
        if self._access_count - last._accessed_at > self._purge_point:
            self._data.delete(last)

    def remove(self, e):
        p = self._find_position(e)
        if p is not None:
            self._data.delete(p)

    def top(self, k):
        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")
        walk = self._data.first()
        for _ in range(k):
            item = walk.element()
            yield item._value
            walk = self._data.after(walk)
