class Tree:
    """Abstract base class representing a tree"""

    class Position:

        def element(self):
            raise NotImplementedError("must be implemented by subclass")

        def __eq__(self, other):
            raise NotImplementedError("must be implemented by subclass")

        def __ne__(self, other):
            return not (self == other)

    # -------- abstract methods that the concrete subclass must support ------
    def root(self):
        raise NotImplementedError('must be implemented by subclass')

    def parent(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def num_children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def children(self, p):
        raise NotImplementedError('must be implemented by subclass')

    def __len__(self):

        raise NotImplementedError('must be implemented by subclass')

    def is_root(self, p):
        return self.root() == p

    def is_leaf(self, p):
        return self.num_children(p) == 0

    def is_empty(self):
        return len(self) == 0

    # ---- concrete implementations ----

    def depth(self, p):
        """
        The depth of p is that number of ancestors of p, exluding p itself
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """
        Height is the max number of ancestors of any leaf of a tree

        The method below is not very efficient
        assuming self.positions is O(n):
            coz height1 calls the algo depth(p) on each leaf of the tree
            its running time is O(n + running time of calc depth of all leafs)
            which makes it O(n^2)
        """
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))

    def _height2(self, p):
        """
        This method of calculating height is O(n)
        """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))

    def height(self, p = None):
        if p is None:
            p = self.root()
        return self._height2(p)
