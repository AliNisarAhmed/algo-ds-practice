"""
Favorite list with Move to Front heuristic

When an element is accessed, it is moved to the top of the linked list, 
since it is more likely to be accessed again
"""

from favorites_list import FavoritesList
from positional_list import PositionalList


class FavoritesListMTF(FavoritesList):
    def _move_up(self, p):
        if p != self._data.first():
            # delete/reinsert at first pos
            self._data.add_first(self._data.delete(p))

    def top(self, k):
        """Generate a sequence of top k elements sorted in terms of access count"""

        if not 1 <= k <= len(self):
            raise ValueError("Illegal value for k")

        temp = PositionalList()

        # Copy the original list
        for item in self._data:
            temp.add_last(item)

        for _ in range(k):
            highPos = temp.first()
            walk = temp.after(highPos)

            # traverse temp and find the element with highest count
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)

            # we have found the element with highest count
            yield highPos.element()._count  # report element to the user
            temp.delete(highPos)  # remove from temp list


# R-7.20
# Accessing elements in their current order will reverse the list
# e.g. { a b c }
# access a -> a b c
# access b -> b a c
# access c -> c b a


# R-7.21
# lets say we have n elements in order 1..n
# access each in order 1..n
# then again access in order 1..n
# total accesses: 2n times (1 + 2 + 3 + n) -> 2n (n (n + 1)) -> O(N^3)
