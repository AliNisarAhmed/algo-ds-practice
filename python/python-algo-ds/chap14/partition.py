class Partition:
    """Union-find structure for maintaining disjoint sets"""

    # ---- Nested Position class ----

    class Position:
        __slots__ = '_container', '_element', '_size', '_parent'

        def __init__(self, container, e):
            """Create a new position that is the leader of its own group
            """
            self._container = container
            self._element = e
            self._size = 1
            self._parent = self  # convention for group leader

        def element(self):
            return self._element

    def make_group(self, e):
        """Makes a new group containing element e, and returns its Position"""
        return self.Position(self, e)

    def find(self, p):
        """Finds the group containing p and return the leader's position"""
        if p._parent != p:
            # overwrite p._parent after recursion
            p._parent = self.find(p._parent)
        return p._parent

    def union(self, p, q):
        """Merges the groups containing element p & q (if distinct)"""
        a = self.find(p)
        b = self.find(q)

        if a is not b:
            if a._size > b._size:
                b._parent = a
                a._size += b._size
        else:
            a._parent = b
            b._size += a._size
