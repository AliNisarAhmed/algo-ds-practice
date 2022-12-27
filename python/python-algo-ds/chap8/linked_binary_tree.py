from binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    class _Node:
        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """Return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:  # a convention usef for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    # ---- Binary Tree constructor ----

    def __init__(self):
        self._root = None
        self._size = 0

    # ---- Public Accessors ----

    def __len__(self):
        return self._size

    def root(self):
        return self._make_position(self._root)

    def parent(self, p):
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        node = self._validate(p)
        count = 0
        if node._left is not None:
            count += 1
        if node._right is not None:
            count += 1

        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position"""
        if self._root is not None:
            raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        node = self._validate(p)
        if node._left is not None:
            raise ValueError("Left child exists")
        self._size += 1
        node._left = self._Node(e, node)
        return self._make_position(node._left)

    def _add_right(self, p, e):
        node = self._validate(p)
        if node._right is not None:
            raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e, node)
        return self._make_position(node._right)

    def _replace(self, p, e):
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """
        Delete the node at Position p, and replace it with its child, if any
        Note: deletes only when a node has 1 children, throws in case of two children
        """

        node = self._validate(p)

        if self.num_children(p) == 2:
            raise ValueError("p has two children")

        child = node._left if node._left else node._right

        if child is not None:
            child._parent = node._parent  # childs grandparent becomes parent

        if node is self._root:
            self._root = child
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child

        self._size -= 1
        node._parent = node  # convention for deprecated nodes

        return node._element

    def _attach(self, p, t1, t2):
        """Attach trees t1 and t2 as left and right subtrees of external node p"""

        node = self._validate(p)

        if not self.is_leaf(p):
            raise ValueError("position must be leaf")

        if not type(self) is type(t1) is type(t2):
            raise TypeError("Tree types must match")

        self._size += len(t1) + len(t2)

        if not t1.is_empty():
            t1._root._parent = node
            node._left = t1._root
            t1._root = None
            t1._size = 0

        if not t2.is_empty():
            t2._root._parent = node
            node._right = t2._root
            t2._root = None
            t2._size = 0

    # C-8.38
    def _delete_subtree(self, p):
        parent = self.parent(p)

        if p == self.left(parent):
            parent._node._left = None
        else:
            parent._node._right = None

        self._size = len(list(self.positions()))


# R-8.15
class MutableLinkedBinaryTree(LinkedBinaryTree):
    """
    A class that provides public mutators of the LinkedBinaryTree class
    """

    def add_root(self, e):
        return self._add_root(e)

    def add_left(self, p, e):
        return self._add_left(p, e)

    def add_right(self, p, e):
        return self._add_right(p, e)

    def replace(self, p, e):
        return self._replace(p, e)

    def delete(self, p):
        return self._delete(p)

    def attach(self, p, t1, t2):
        return self._attach(p, t1, t2)


if __name__ == "__main__":
    t = MutableLinkedBinaryTree()
    root = t.add_root(1)
    two = t.add_left(root, 2)
    three = t.add_right(root, 3)

    t.add_left(two, 4)
    t.add_right(two, 5)
    four = t.add_left(three, 6)
    five = t.add_right(three, 7)

    t._add_left(four, 8)
    t._add_left(five, 9)
    t._add_right(four, 10)
    t._add_right(five, 10)

    print(t._size)
    t._delete_subtree(two)
    print(t._size)
    t._delete_subtree(three)
    print(t._size)


# R-8.16
# Level numbering function f

# let f(p) be an integer defined as:

# if p is root, then f(p) = 0
# if p is the left child of q, then  f(p) = 2 x f(q) + 1
# if p is the right child of q, then f(p) = 2 x f(q) + 2

# Now show that
# for every position p of T, f(p) <= 2^n - 2
# Show an example of a BT with 7 nodes that attains the above upper bound on f(p)
