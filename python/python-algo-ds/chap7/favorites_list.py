from positional_list import PositionalList
class FavoritesList:
    """List of elements orderd from most frequently accessed to least"""

    class _Item:
        __slots__ = '_value', '_count'

        def __init__(self, e):
            self._value = e
            self._count = 0

    def __init__(self):
        self._data = PositionalList()

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
            count = p.element()._count
            walk = self._data.before(p)

            if count > walk.element()._count:
                while (walk != self._data.first() and 
                        count > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(p)) # delete/reinsert

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e):
        """Access element e, thereby increasing its access count"""

        p = self._find_position(e)

        if p is None:
            p = self._data.add_last(self._Item(e))

        p.element()._count += 1
        self._move_up(p)

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
