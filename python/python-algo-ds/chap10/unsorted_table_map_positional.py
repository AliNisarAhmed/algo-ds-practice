import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from chap7.positional_list import PositionalList
from map_base import MapBase

class UnsortedTableMapPositional(MapBase):

    def __init__(self) -> None:
        self._table = PositionalList()

    def __getitem__(self, k):
        for item in self._table:
            if item._key == k:
                return item._value

        raise KeyError("Key Error " + repr(k))

    def __setitem__(self, k, v):
        for item in self._table:
            if item._key == k:
                item._value = v
                return
        self._table.add_last(self._Item(k, v))

    def __delitem__(self, k):
        curr = self._table.first()
        while curr is not None:
            if curr.element()._key == k:
                result = curr.element()
                self._table.delete(curr)
                return result._value
            else:
                curr = self._table.after(curr)
        return None

    def __iter__(self):
        for item in self._table:
            yield item

    def __len__(self):
        return len(self._table)


if __name__ == "__main__":
    m = UnsortedTableMapPositional()
    m.__setitem__(1, 100)
    m.__setitem__(2, 200)
    m.__setitem__(3, 300)

    print(m.__getitem__(1))
    print(m.__getitem__(2))

    print(m.__delitem__(3))
    print(m.__getitem__(3))
