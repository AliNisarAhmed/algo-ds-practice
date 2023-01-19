from sorted_table_map import SortedTableMap

class CostPerformanceDatabase:
    """Maintain a DB of maximal (cost, performance) pairs"""

     def __init__(self):
         self._M = SortedTableMap()

     def best(self, c):
         """Return (cost, performance) pair with largest cost not exceeding c
            
            Return None if there is no such pair
         """
         return self._M._find_le(c)

     # add has O(N) worst-case time because of SortedTableMap
     # using skip list can improve it
     def add(self, c, p):
        """add new entry with cost c and performance p"""

        other = self._M.find_le(c) # other is at least as cheap as c
        if other is not None and other[1] >= p: # if its performance is as good
            return  # (c,p) is dominated, so ignore
        self._M[c] = p
        # and now remove any pairs dominated by (c,p)
        other = self._M.find_gt(c)
        while other is not None and other[1] <= p:
            del self._M[other[0]]
            other = self._M.find_gt(c)
