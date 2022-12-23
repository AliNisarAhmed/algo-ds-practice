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
