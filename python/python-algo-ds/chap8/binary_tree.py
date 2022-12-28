"""
A binary tree is an ordered tree with the following properties
1. Every node has at most two children
2. Each node is labled as being a left child or a right child
3. A left child precedes a right child in the oder of children of a node

A tree is proper if each node has either 0 or two children

## Binary Tree Properties

T  = nonempty BT
n  = number of nodes
ne = number of external nodes (leaves)
ni = number of internal nodes (non-leaves)
h  = height of tree (height of root node is 0)

Properties:
    1. h + 1 <= n <= 2^(h + 1) - 1
    2. 1 <= ne <= 2^h
    3. h <= ni <= 2^h - 1
    4. log(n + 1) - 1 <= h <= n - 1

If T is proper: than following additional properties:
    1. 2h + 1 <= n <= 2^(h + 1) - 1
    2. h + 1 <= ne <= 2^h
    3. h <= ni <= 2^h - 1
    4. log(n + 1) - 1 <= h <= (n - 1) / 2
    5. ne = ni + 1
"""

from tree import Tree


class BinaryTree(Tree):
    """
    Abstract class
    """

    # ---- additional abstract methods ----

    def left(self, p):
        """Return p's left child"""
        raise NotImplementedError("must be implemented by a subclass")

    def right(self, p):
        """Return p's right child"""
        raise NotImplementedError("must be implemented by a subclass")

    # ---- concrete methods implemented in this class ----

    def sibling(self, p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)

    def children(self, p):
        """generate an iteration of Positions representing p's children"""
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    # R-8.5
    def _count_left_leaves_rec(self, p):
        if p is None:
            return 0

        left_child = self.left(p)
        count = 0

        if left_child is not None and len(list(self.children(left_child))) == 0:
            count += 1

        for c in self.children(p):
            count += self._count_left_leaves_rec(c)

        return count

    def count_left_leaves(self):
        return self._count_left_leaves_rec(self.root())

    def inorder(self):
        """
        Inorder:
            visit root after ALL the positions in the Left subtree,
            but before ALL the positions in the right subtree

        Inorder traversal can only be applied to Binary Trees (since they have order)
        Example: Evaluating math expressions uses inorder traversal
        """

        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):

        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other

        yield p

        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other

    def positions(self):
        return self.inorder()

    def print(self):
        for p in self.positions():
            print(p.element(), end=" -> ")
        print("--- end tree--")

    # R-8.10
    def num_children(self, p):
        count = 0
        if self.left(p) is not None:
            count += 1
        if self.right(p) is not None:
            count += 1

        return count


# R-8.7
# What is the max and min of number of internal and external nodes
# in an improper binary tree with n nodes
# Answer
# Max of internal = n - 1 (just have a straight line of nodes)
# Min of internal = (n - 1) / 2
# Max of external = (n + 2) / 2
# Min of external = 1 (When internal are max, external are min, so the first case above)

# R-8.8
# What is the minimum number of external nodes for a proper BT with height h:
# h - 1
# What is the max number of external nodes for a proper BT with height h
# 2^h

# R-8.12
# Expression is (6 / (1 - (5 / 7)))

# ------------------------------------------------------------------------------------------

# R-8.18
# Array based BT representation pseudo-algos

# def root(self, p):
#     return self._data[0]
#
# def parent(self, p):
#     if p.level is odd:
#         return p.level - 1 / 2
#     else:
#         reurn p.level - 2 / 2
#
# def left(self, p):
#     return p.level * 2 + 1
#
# def right(self, p):
#     return p.level * 2 + 2
#
# def is_leaf(self, p):
#     return self.left(p) is None and self.right(p) is None
#
# def is_root(self, p):
#     return p.level == 0
