from sorted_table_map import SortedTableMap


class CostPerformanceDatabase:
    """Maintain a DB of maximal (cost, performance) pairs"""

    def __init__(self):
        self._M = SortedTableMap()

    def best(self, c):
        """Return (cost, performance) pair with largest cost not exceeding c

           Return None if there is no such pair
        """
        return self._M.find_le(c)

    # add has O(N) worst-case time because of SortedTableMap
    # using skip list can improve it
    def add(self, cost, performance):
        """add new entry with cost c and performance p"""

        other = self._M.find_le(cost)  # other is at least as cheap as c
        # if its performance is as good
        if other is not None and other[1] >= performance:
            return  # (c,p) is dominated, so ignore
        self._M[cost] = performance
        # and now remove any pairs dominated by (c,p)
        other = self._M.find_gt(cost)
        while other is not None and other[1] <= performance:
            del self._M[other[0]]
            other = self._M.find_gt(cost)


if __name__ == "__main__":
    db = CostPerformanceDatabase()
    db.add(10000, 8)
    db.add(11000, 7)
    db.add(12000, 5)
    db.add(12000, 6)
    db.add(12500, 7)

    db._M.print()
    print(db._M.find_gt(12000))

# R-10.22
# Q: wat is the expected running time of the add method above
#    if we insert n pairs such that each pair has lower cost and performance than one before it
#    ex: [2000, 3], [1500, 2], [1000, 1]
# A: if using SortedTableMap
#     - O(n^2)
#    if using SkipList
#    - O(nlogn)
