import types
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
            self._height = 0

        def element(self):
            return self._node._element

        def __eq__(self, other):
            return type(other) is type(self) and other._node is self._node

        def set_height(self, h):
            self._height = h

    def _validate(self, p):
        """Return associated node, if position is valid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._parent is p._node:  # a convention used for deprecated nodes
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
        if node._right is not None:
            count += 1

        if node._left is not None:
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
        """Create a new left child for Position p, storing element e"""
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

    def _size_subtree(self, p):
        if p is None:
            return 0

        if self.is_leaf(p):
            return 1

        count = 1
        for c in self.children(p):
            count += self._size_subtree(c)

        return count

    # C-8.38
    def _delete_subtree(self, p):
        parent = self.parent(p)

        if p == self.left(parent):
            parent._node._left = None
        else:
            parent._node._right = None

        # self._size = len(list(self.positions()))
        self._size -= self._size_subtree(p)

    # C-8.39
    def _swap(self, p, q):
        p_element = p._node._element
        p._node._element = q._node._element
        q._node._element = p_element

    # --------------------------------------------------------------------------
    # C-8.50
    # Design algos for preorder_next, inorder_next and postorder_next
    # and what are their worst-case running times

    # Worst case for all these algos is O(h) where h is height of the tree
    def preorder_next(self, p):
        left = self.left(p)
        if left is not None:
            return left

        right = self.right(p)
        if right is not None:
            return right

        # return right child available of first ancestor up the chain
        return self._first_right_ancestor(p)

    def _first_right_ancestor(self, p):
        if p is None:
            return None

        parent = self.parent(p)

        if parent is None:
            return None

        right_sibling = self.right(parent)
        if right_sibling != p:
            return right_sibling
        else:
            return self._first_right_ancestor(parent)

    def inorder_next(self, p):
        right = self.right(p)
        if right is not None:
            return self._left_most(right)

        return self._first_ancestor_not_right_child(p)

    def _first_ancestor_not_right_child(self, p):
        if p is None:
            return None
        parent = self.parent(p)

        if parent is None:
            return None

        if self.right(parent) == p:
            return self._first_ancestor_not_right_child(parent)
        else:
            return parent

    def postorder_next(self, p):
        parent = self.parent(p)
        if parent is None:
            return None

        if self.right(parent) == p:
            return parent
        else:
            return self._left_most(self.right(parent))

    def _left_most(self, p):
        if p is None:
            return p

        if self.left(p) is not None:
            return self._left_most(self.left(p))

        return p

    # -------------------------------------------------------------------------


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


# C-8.35
def are_trees_isomorphic(t1, t2):
    return _are_trees_isomorphic(t1, t1.root(), t2, t2.root())


def _are_trees_isomorphic(t1, p1, t2, p2):
    p1_empty = p1 is None
    p2_empty = p2 is None

    if (p1_empty and p2_empty):
        return True

    if (p1_empty and not p2_empty):
        return False

    if (not p1_empty and p2_empty):
        return False

    t1_childen = list(t1.children(p1))
    t2_children = list(t2.children(p2))

    if t1_childen != t2_children:
        return False

    for (c1, c2) in zip(t1_childen, t2_children):
        res = _are_trees_isomorphic(t1, c1, t2, c2)

        if res is False:
            return False

    return True


# C-8.40
class SentinelLinkedBinaryTree:
    def __init__(self):
        self._sentinal = types.SimpleNamespace()

    def _add_root(self, e):
        if self._sentinel._left is not None:
            raise ValueError("Root already exists")
        self._sentinel._left = self._Node(e)
        self._size = 1
        return self._make_position(self._root)

    def _delete(self, p):
        self._validate(p)
        if self.num_children(p) == 2:
            raise ValueError("Cannot delete with two children")


# C-8.41 - clone using _attach
def clone(t: LinkedBinaryTree) -> LinkedBinaryTree:
    def _clone(
        t: LinkedBinaryTree, p: LinkedBinaryTree.Position | None
    ) -> LinkedBinaryTree:
        if p is None:
            return LinkedBinaryTree()

        new_tree = LinkedBinaryTree()
        new_root = new_tree._add_root(p.element())

        new_tree._attach(new_root, _clone(t, t.left(p)), _clone(t, t.right(p)))

        return new_tree

    return _clone(t, t.root())


# C-8.42 - clone using add_left and add_right
def clone2(t: LinkedBinaryTree) -> LinkedBinaryTree:
    def _clone(old_tree, old_p, new_tree, new_p):
        if old_p is None:
            return

        old_left = old_tree.left(old_p)
        old_right = old_tree.right(old_p)

        if old_left is not None:
            new_left = new_tree._add_left(new_p, old_left.element())
            _clone(old_tree, old_left, new_tree, new_left)

        if old_right is not None:
            new_right = new_tree._add_right(new_p, old_right.element())
            _clone(old_tree, old_right, new_tree, new_right)

    old_root = t.root()
    new_tree = LinkedBinaryTree()
    new_root = new_tree._add_root(old_root.element())

    _clone(t, old_root, new_tree, new_root)

    return new_tree


#

# C-8.43
# preorder:  ABEFCDG vs ABEFCDG (match)
# postorder: EFBCGDA vs FEGDCBA (no match)
# inorder:   EBFACDG vs EFBCGDA (same as postorder of the left one)


if __name__ == "__main__":
    t = LinkedBinaryTree()
    root = t._add_root(1)
    print('is_root', t.is_root(root))
    two = t._add_left(root, 2)
    three = t._add_right(root, 3)

    four = t._add_left(two, 4)
    five = t._add_right(two, 5)
    six = t._add_left(three, 6)
    seven = t._add_right(three, 7)

    eight = t._add_left(six, 8)
    nine = t._add_left(seven, 9)
    ten = t._add_right(six, 10)
    eleven = t._add_right(seven, 11)

    print('---- R-8.5 ----')
    # t._add_left(five, 12)

    print('left leaves: ', t.count_left_leaves())

    print('--------')

    print('---- C-8.35 ----')

    t1 = LinkedBinaryTree()
    t2 = LinkedBinaryTree()

    print('isomorphic?', are_trees_isomorphic(t1, t2))

    root1 = t1._add_root(1)

    print('isomorphic?', are_trees_isomorphic(t1, t2))

    root2 = t2._add_root(100)
    print('isomorphic?', are_trees_isomorphic(t1, t2))

    left1 = t1._add_left(root1, 2)
    print('isomorphic?', are_trees_isomorphic(t1, t2))

    print('--------')

    # print("before swap: ")
    # t.print()
    # t._swap(three, seven)
    # print("after swap: ")
    # t.print()

    # print(t._size)
    # t._delete_subtree(two)
    # print(t._size)
    # t._delete_subtree(three)
    # print(t._size)

    # cloned_t = clone(t)
    # t.print()
    # cloned_t.print()
    # cloned_t._root._element = 15
    # t.print()
    # cloned_t.print()

    # cloned_t = clone2(t)
    # t.print()
    # cloned_t.print()
    # cloned_t._root._element = 15
    # t.print()
    # cloned_t.print()

    # ---------------------------------
    # t.print_p_and_depth()
    # t.print_p_and_height()
    # print(f"Path Length: {t.path_length()}")
    # ---------------------------------------

    # C-8.50 Testing
    # p = t.inorder_next(root)
    # print(p.element() if p is not None else None)

    # -----------------------------------------------

    # print('--------')
    # print('---- 8.38 ----')
    #
    # t.print()
    # print('tree size: ', t._size)
    # t._delete_subtree(six)
    # t.print()
    # print('tree size: ', t._size)

    # ------------------------------------------------

    print('--------')
    print('---- 8.44 ----')

    t.print_p_and_height()

    # ------------------------------------------------




# R-8.16
# Level numbering function f

# let f(p) be an integer defined as:

# if p is root, then f(p) = 0
# if p is the left child of q, then  f(p) = 2 x f(q) + 1
# if p is the right child of q, then f(p) = 2 x f(q) + 2

# Now show that
# 1.for every position p of T, f(p) <= 2^n - 2
# [1, 2, 3, 4, 5, 6] = n = 6
# [0, 1, 2, 3, 4, 5] ~~ [60, 60, 60, 60, 60, 60]

# 2.Show an example of a BT with 7 nodes that attains the above upper bound on f(p)
# upper bound = 2^7 - 2 = 126
# It's a BT with 7 Right childs only
