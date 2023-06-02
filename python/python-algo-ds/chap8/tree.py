# from ..chap7 import linkedQueue as LQ


class LinkedQueue:
    pass


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
        raise NotImplementedError("must be implemented by subclass")

    def parent(self, p):
        raise NotImplementedError("must be implemented by subclass")

    def num_children(self, p):
        raise NotImplementedError("must be implemented by subclass")

    def children(self, p):
        raise NotImplementedError("must be implemented by subclass")

    def __len__(self):

        raise NotImplementedError("must be implemented by subclass")

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
        Height is the distance to the farthest leaf

        Height is equal to the maximum of the depths of its leaf positions

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

    def height(self, p=None):
        if p is None:
            p = self.root()
        return self._height2(p)

    def __iter__(self):
        for p in self.positions():
            yield p.element()

    def preorder(self):
        """
        Generate preorder iteration of positions in this tree

        Preorder: The root is visited first, then the children are visited in order (left then right)"""

        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self, p):
        yield p  # visit p before its subtree rooted at p
        for c in self.children(p):  # for each child p
            # do preorder of c's subtree
            for other in self._subtree_preorder(c):
                yield other  # yielding each to our caller

    def positions(self):
        return self.preorder()  # return entire preorder iteration

    def postorder(self):
        """
        PostOrder: Opposite of pre-order, visit children in order (left then right), then visit the root
        """

        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p

    def breadthfirst(self):
        if not self.is_empty():
            fringe = LinkedQueue()
            fringe.enqueue(self.root())
            while not fringe.is_empty():
                p = fringe.dequeue()
                yield p
                # R-8.26
                # p.extend(self.children(p))
                for c in self.children(p):
                    fringe.enqueue(c)

    def _print_p_and_height(self, p):
        if self.is_leaf(p):
            print(f"P = {p.element()} with height = {0}")
            return 0
        height = 1 + max([self._print_p_and_height(c)
                         for c in self.children(p)])
        print(f"P = {p.element()} with height = {height}")
        return height

    # C-8.44
    def print_p_and_height(self):
        return self._print_p_and_height(self.root())

    def _print_p_and_depth(self, p, depth):
        if p is None:
            return depth
        print(f"p is {p.element()} with depth = {depth}")

        for c in self.children(p):
            self._print_p_and_depth(c, depth + 1)

    # C-8.45
    def print_p_and_depth(self):
        return self._print_p_and_depth(self.root(), 0)

    # C-8.46
    # Path length is the sum of the depths of all positions in T
    def path_length(self):
        _, pl = self._path_length(self.root(), 0)
        return pl

    def _path_length(self, p, depth):
        if self.is_leaf(p):
            return (depth, 0)

        path_length = 0
        for c in self.children(p):
            (d, pl) = self._path_length(c, depth + 1)
            path_length = path_length + d + pl

        return (depth, path_length)


# R-8.6
# Since if we add a node to any improper tree, it will become proper,
# we can achieve the goal using a sentinel node at the root of T'

# R-8.21
# R-8.22
# Pre-order: -/x+313+-952+x37-46
# Postorder: 31+3x95-2+/374-x6+-
# Inorder:   3+1x3/9-5+2/3x7-4+6

# R-8.23
# Is it possible for postorder and preorder to be the same for a tree with more than 1 node?
# No
# Is it possible for postorder and preorder to be reverse?
# Yes - Example - tree with 2 nodes

# R-8.24
# Above questions for proper BTs
# Answer: No and No

# R-8.25
# {1}
# {2, 3 , 4}
# {3, 4, 5, 6}
# {4, 5, 6, 7, 8, 9, 10, 11}
# {5, 6, 7, 8, 9, 10, 11}
# {6, 7, 8, 9, 10, 11}
# ... and so on to {}
