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
