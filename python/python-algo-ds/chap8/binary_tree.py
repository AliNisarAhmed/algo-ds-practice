"""
A binary tree is an ordered tree with the following properties
1. Every node has at most two children
2. Each node is labled as being a left child or a right child
3. A left child precedes a right child in the oder of children of a node
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
