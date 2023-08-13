"""
A Red-Black tree is a BST with nodes colored wither red or black with the following properties:
    - Root Property:
        The root is black
    - Red Property: 
        The children of a red node (if any) are black
    - Depth Property:
        All noes with 0 or 1 children have the same `black depth`,
            defined as the number of black ancestors (including itself)

Wikipedia defines the Red-Black tree properties as follows:
    - Every node is either Red or Black
    - All NIL (empty child nodes of external nodes) are considered black
    - a red node does not have a red child
    - Every path from a node to its descendent NIL node goes thru the same number of black nodes
    - if a node has exactly 1 child, it must be red

Relation with (2,4) trees:
    - a Red-Black tree can be converted to a (2,4) tree by merging every red node w into its parent,
        storing the entry from w at its parent, 
        and with the children of w becoming ordered children of the parent


Proposition: The height of a Red-Black tree storing n entries is O(log n)
"""

from tree_map import TreeMap


class RedBlackTree(TreeMap):
    """Sorted map implementation using a red-black tree"""

    class _Node(TreeMap._Node):
        """Node class for red-black tree maintains bit that denotes color"""
        __slots__ = '_red'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._red = True  # new node is red by default

    # ------------------- positional-based utility methods -------------------
    # we consider a nonexistence child to be trivially black
    def _set_red(self, p): p._node._red = True
    def _set_black(self, p): p._node._red = False
    def _set_color(self, p, make_red): p._node._red = make_red
    def _is_red(self, p): return p is not None and p._node._red

    def _get_red_child(self, p):
        """Return a red child of p (or None if no such child)"""
        for child in (self.left(p), self.right(p)):
            if self._is_red(child):
                return child
        return None

    # -------------------- Support for insertions -----------------------------

    def _rebalance_insert(self, p):
        self._resolve_red(p)  # new node is always red

    def _resolve_red(self, p):
        if self.is_root(p):
            self._set_black(p)  # make root black
        else:
            parent = self.parent(p)
            if self._is_red(parent):  # double red problem
                uncle = self.sibling(parent)
                if not self._is_red(uncle):
                    # Case 1: misshapen 4-node / trinode restructuring
                    middle = self._restructure(p)  # do trinode restructuring
                    self._set_black(middle)  # then fix colors
                    self._set_red(self.left(middle))
                    self._set_red(self.right(middle))
                else:
                    # Case 2: overfull 5-node / recoloring
                    grand = self.parent(parent)
                    self._set_red(grand)  # grandparent becomes red
                    # its children become black
                    self._set_black(self.left(grand))
                    self._set_black(self.right(grand))
                    # recur at red grandparent
                    self._resolve_red(grand)

    # ---------------------- Support for deletions ---------------------------
    def _rebalance_delete(self, p):
        if len(self) == 1:
            # special case: ensure that root is black
            self._set_black(self.root())
        elif p is not None:
            n = self.num_children(p)
            if n == 1:  # deficit exists unless child is a red leaf
                c = next(self.children(p))
                if not self._is_red_leaf(c):
                    self._fix_deficit(p, c)
            elif n == 2:
                if self._is_red_leaf(self.left(p)):
                    self._set_black(self.left(p))
                else:
                    self._set_black(self.right(p))

    def _fix_deficit(self, z, y):
        """Resolve black deficit at z, where y is the root of z's heavier subtree"""
        if not self._is_red(y):
            # y is black; will apply Case 1 or 2
            x = self._get_red_child(y)
            if x is not None:
                # Case 1: y is black and has red child x
                # do a transfer
                old_color = self.is_red(z)
                middle = self._restructure(x)
                # middle gets old color of z
                self._set_color(middle, old_color)
                # children become black
                self._set_black(self.left(middle))
                self._set_black(self.right(middle))
            else:
                # Case 2: y is black but no red children
                # recolor as "Fusion"
                set._set_red(y)
                if self.is_red(z):
                    # this resolves the problem
                    self._set_black(z)
                elif not self.is_root(z):
                    # recur upward
                    self._fix_deficit(self.parent(z), self.sibling(z))
        else:
            # Case 3: y is red, rotate misaligned 3-node and repeat
            self._rotate(y)
            self._set_black(y)
            self._set_red(z)
            if z == self.right(y):
                self._fix_deficit(z, self.left(z))
            else:
                self._fix_deficit(z, self.right(z))
