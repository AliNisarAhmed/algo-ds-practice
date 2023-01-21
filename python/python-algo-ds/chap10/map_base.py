from collections.abc import MutableMapping


class MapBase(MutableMapping):
    """Abstract base class that includes a non-public _Item class

    MutableMapping class provides 5 significant beaviours:
    1. M[k]
    2. M[k] =  v
    3. del M[k]
    4. len(M)
    5. iter(M)
    """

    class _Item:

        __slots__ = "_key", "_value"

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key

        def __ne__(self, other):
            return not (self == other)

        def __lt__(self, other):
            return self._key < other._key

    # R-10.1 implement pop(k, d=None)
    def pop(self, k, default_val=None):
        """Remove item associated with k and return its value
        if key not in map, return default_val if it is not None
        else raise KeyError
        """
        try:
            val = self[k]
            del self[k]
            return val
        except KeyError as ex:
            if default_val is not None:
                return default_val
            raise ex

    # R-10.2 implement items()
    # Runs in O(n^2) for UnsortedTableMap coz of O(n) self[k] access for each k
    def items(self):
        for k in self:
            yield (k, self[k])
