from tree import Tree
import math


class ArrayBinaryTree(Tree):
    def __init__(self):
        self._data = []

    class _Node:
        __slots__ = "_element", "_parent", "_left", "_right"

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(Tree.Position):
        """An abstraction representing the location of a single element"""

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

    # -----------------------------------------------

    def _find_index(self, p):
        return self._data.index(p._node)

    def _get_at_index(self, i):
        try:
            node = self._data[i]
            return self._make_position(node)
        except IndexError:
            return None

    def _make_position(self, node):
        return self.Position(self, node) if node is not None else None

    def _add_at_index(self, e, index):
        if index >= len(self._data):
            copy = [None] * (index + 1)
            for i in range(len(self._data)):
                copy[i] = self._data[i]
            self._data = copy

        node = self._Node(e)
        self._data[index] = node

        return node

    # ---------------------------------------------

    def root(self):
        return self._make_position(self._get_at_index(0))

    def parent(self, p):
        parent_idx = (self._find_index(p) - 1) // 2
        return self._get_at_index(parent_idx)

    def left(self, p):
        return self._get_at_index(self._find_index(p) * 2 + 1)

    def right(self, p):
        return self._get_at_index(self._find_index(p) * 2 + 2)

    def sibling(self, p):
        parent = self.parent(p)
        if self.left(parent) == p:
            return self.right(parent)
        else:
            return self.left(parent)

    def children(self, p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def num_children(self, p):
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1

        return count

    def __len__(self):
        return len(self._data)

    def is_root(self, p):
        return self._get_at_index(0) == p

    def is_empty(self):
        return len(self) == 0

    def is_leaf(self, p):
        if self.left(p) is None and self.right(p) is None:
            return True

        return False

    def add_root(self, e):
        if self.root() is not None:
            raise ValueError("root is already present")

        node = self._add_at_index(e, 0)
        return self._make_position(node)

    def add_left(self, p, e):
        left_index = self._find_index(p) * 2 + 1
        node = self._add_at_index(e, left_index)
        return self._make_position(node)

    def add_right(self, p, e):
        right_index = self._find_index(p) * 2 + 2
        node = self._add_at_index(e, right_index)
        return self._make_position(node)


if __name__ == "__main__":
    t = ArrayBinaryTree()
    root = t.add_root(1)
    two = t.add_left(root, 2)
    three = t.add_right(root, 3)
    four = t.add_left(two, 4)
    five = t.add_right(two, 5)

    print(
        t.left(root).element(),
        t.right(root).element(),
        t.left(two).element(),
        t.right(two).element(),
        t.left(three),
        t.right(three),
        t.parent(three).element(),
    )
