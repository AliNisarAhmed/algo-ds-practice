class MultiMap:
    """A mulimap is similar to a map, except that in multimap
    one key can be associated with multiple values

    for example, index of a book, linking a topic to multiple pages,
    is a multimap
    """

    _MapType = dict  # Map Type, can be redefined by subclass

    def __init__(self):
        self._map = self._MapType()  # create map instance for storage
        self._n = 0

    def __iter__(self):
        for k, secondary in self._map.items():
            for v in secondary:
                yield (k, v)

    def add(self, k, v):
        container = self._map.setdefault(k, [])  # create empty list, if key not found
        container.append(v)
        self._n += 1

    def pop(self, k):
        secondary = self._map[k]
        v = secondary.pop()
        if len(secondary) == 0:
            del self._map[k]
        self._n -= 1
        return (k, v)

    def find(self, k):
        secondary = self._map[k]
        return (k, secondary[0])

    def find_all(self, k):
        secondary = self._map.get(k, [])  # empty list by default
        for v in secondary:
            yield (k, v)
