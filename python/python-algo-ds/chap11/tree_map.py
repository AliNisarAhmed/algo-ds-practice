
import pathmagic
from chap8.linked_binary_tree import LinkedBinaryTree
from chap10.map_base import MapBase


class TreeMap(LinkedBinaryTree, MapBase):
    """Sorted map implementation using a binary search tree

    We use inorder traversal since it results in a sorted ordered traversal
    of a tree
    """

    # ---- overriding Position class ----
    class Position(LinkedBinaryTree.Position):
        def key(self):
            return self.element()._key

        def value(self):
            return self.element()._value

    # ---- non-public utilities ----

    def _subtree_search(self, p: Position, k):
        """Return Position of p's subtree having key k, or last node searched"""
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)
        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)

    def _subtree_first_position(self, p):
        """Return Position of first item in subtree rooted at p"""
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """Return Position of last item in subtree rooted at p"""
        walk = p
        while self.right(p) is not None:
            walk = self.right(p)
        return walk

    # ---- public methods ----

    def first(self):
        """Return the first position in the tree (inorder traversal)"""
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """Return the last position in the tree (inorder traversal)"""
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """Return the Postion just before p in inorder traversal

        Return None if p is the first position
        """
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward (till first right child)
            # till we find a parent that is a right child of its parent
            walk = p
            above = self.parent(p)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """Return the Position just after p in inorder traversal

        Return None if p is the last position
        """
        self._validate(p)
        if self.right(p):
            return self._subtree_first_position(self.right(p))
        else:
            walk = p
            above = self.parent(p)
            while above is not None and walk == self.right(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """Return position with key k, or else neighbor (or None if empty)"""
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)  # hook for balanced tree subclasses
            return p

    def find_min(self):
        """Return (key, value) pair with minimum key (or None if empty)"""
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        """Return KV pair with least key >= k

        Return None if there does not exist such a key
        """
        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                # p's key is too small, thus fetch the next in order which should be > p
                p = self.after(p)
            return (p.key(), p.value()) if p is not None else None

    def find_range(self, start, stop):
        """Iterate all KV pairs such that start <= key < stop

        If start is None, iteration begins with the minimum key of the map
        It stop is None, iteration cotinues till the max key of the map
        """
        if not self.is_empty():
            if start is None:
                p = self.first()

            else:
                # we find the starting point similar in logic to find_ge
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        """Return value associated with key k (raise KeyError if not found)"""
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)  # hook for balanced tree subclasses
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                # found exact match, replace value
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
            self._rebalance_insert(leaf)  # hook for balanced tree subclasses

    def __iter__(self):
        """Generate an iteration of all keys in the map in order"""
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """Remove the item at given Position p"""
        self._validate(p)
        if self.left(p) and self.right(p):
            # if p has two children
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p)  # inherited from LinkedBinaryTree
        self._rebalance_delete(parent)  # if root deleted, parent is None

    def __delitem__(self, k):
        """Remove item associated with key k (raise KeyError if not found)"""
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError('Key Error: ' + repr(k))

    def print(self):
        p = self.first()
        while p is not None:
            print(p.key())
            p = self.after(p)

    def _relink(self, parent, child, make_left_child):
        """Relink parent node with child node (we allow child to be None)"""
        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            # make child point to parent
            child._parent = parent

    def _rotate(self, p):
        """Rotate Position p above its parent

        the focus of this method is to redefine the relationship
        between the parent and the child, relinking a rotated node directly
        to its original grandparent, and shifting the "middle" subtree between
        rotated nodes (T2 below)

            z
            |
            y
           / \
          x   T3
         / \
        T1  T2


        becomes

            z
            |
            x
           / \
          T1  y
             / \
            T2  T3

        """
        x = p._node
        y = x._parent  # we assume this exists
        z = y._parent  # grandparent (possibly None)
        if z is None:
            self._root = x  # x becomes the root
            x._parent = None
        else:
            # x becomes a direct child of z in the same position as y (left or right)
            self._relink(parent=z,
                         child=x,
                         make_left_child=y == z._left)
        # now rotate x & y, including transfer of middle subtree
        if x == y._left:
            # x._right becomes left child of y
            self._relink(parent=y, child=x._right, make_left_child=True)
            # y becomes right child of x
            self._relink(parent=x, child=y, make_left_child=False)
        else:
            # x._left becomes right child of y
            self._relink(parent=y, child=x._left, make_left_child=False)
            # y becomes left child of x
            self._relink(parent=x, child=y, make_left_child=True)

    def _restructure(self, x):
        """Perform trinode restructure of Position x with parent/grandparent"""
        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):
            # matching alignments, so single rotation
            self._rotate(y)
            # y is new subtree root
            return y
        else:
            # opposite alignments, do double rotation of x
            self._rotate(x)
            self._rotate(x)
            # x is new subtree root
            return x


if __name__ == "__main__":
    print("exec")
    m = TreeMap()
    root = m._add_root(m._Item(15, 'fifteen'))
    ten = m._add_left(root, m._Item(10, 'ten'))
    twenty = m._add_right(root, m._Item(20, 'twenty'))

    m._add_left(ten, m._Item(5, 'five'))
    m._add_right(ten, m._Item(12, 'twelve'))

    m._add_left(twenty, m._Item(18, 'eighteen'))
    m._add_right(twenty, m._Item(22, 'twenty two'))

    m.print()

    print(m.after(ten).key())
