"""
An AVL tree is a Balanced Search tree with the following property:

height-balance property:
    For every position p of T, the heights of the children of p differ by at most 1
    where:
        height of a Position p = max number of nodes from p to a leaf, including p
        Thus, a leaf position has a height of 1

The height of an AVL tree storing n entries is O(log n)

When we detect imbalance in AVL tree, for example:
    - after insertion of position p:
        - We go up from p till we encounter a node z that is unbalanced 
        (i.e, z's child's height are not balanced)
        - let y = z's child with higher height
        - let x = y's child with heigher height
        - we do `trinode restructuring` on x
        - and then continue our search up from x
    - after deletion
        - very similar to above
        - let z be first unbalanced position
        - let y = child of z with higher height
        - let x = child of y with higher height
            - if both children of y have same height
            - prefer x to be on the same side of y as y is to z
        - perform trinode restructuring on x
"""

from tree_map import TreeMap


class AVLTreeMap(TreeMap):
    """Sorted map implementation using an AVL tree"""

    # ---- Nested node class ----

    class _Node(TreeMap._Node):
        """Node class for AVL stores height value for balancing"""
        __slots__ = '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0  # will be recomputed during balancing

        def left_height(self):
            return self._left._height if self._left is not None else 0

        def right_height(self):
            return self._right._height if self._right is not None else 0

    # ---- positional-based utility methods ----

    def _recompute_height(self, p):
        p._node._height = 1 + \
            max(p._node.left_height(), p._node.right_height())

    def _isBalanced(self, p):
        return abs(p._node.left_height() - p._node.right_height()) <= 1

    def _tall_child(self, p, favorleft=False):
        # favorleft param controls tiebreaker
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        # if a child is on left, favor left grandchild, else favor right grandchild
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height  # trivially 0 if new node
            if not self._isBalanced(p):
                # imbalance detected!
                # perform trinode restructuring, setting p to resulting root
                # and recompute new local heights after restructuring
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)  # adjust for recent changes
            if p._node._height == old_height:
                break  # if height has not changed, no further changes needed
            else:
                p = self.parent(p)  # repeat with parent

    # ---- overriding balancing hooks ----

    def _rebalance_insert(self, p):
        self._rebalance(p)

    def _rebalance_delete(self, p):
        self._rebalance(p)


if __name__ == "__main__":
    avl = AVLTreeMap()
    avl[44] = 'root'
    avl[17] = 'seventeen'
    avl[62] = 'sixty-two'
    avl[50] = 'fifty'
    avl[78] = 'seventy-eight'
    avl[48] = 'forty-eight'
    avl[54] = 'fifty-four'
    avl[88] = 'eight-eight'

    avl.print()

    print('--------')

    avl[32] = 'thirty-two'

    avl.print()

    del avl[78]

    print('--------')

    avl.print()
