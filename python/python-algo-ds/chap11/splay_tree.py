"""
Splaying:
    given a node x if a BST T, we splay x by moving x to the root of T
    through a sequence of restructurings

There are 3 cases to condider:
    zig-zig:
        The node x and its parent y are both left children or both right children
        Rotate y first
        then rotate x

                            |
                            z
                           / \
                          T1  y
                             / \
                            T2  x
                               / \
                              T3  T4
        becomes

                            |
                            x
                           / \
                          y  T4
                         / \
                        z   T3
                       / \
                      T1  T2

    zig-zag:
        One of x & y is a left child and the other is a right child
        Double rotate on x

                            |
                            z
                           / \
                          T1  y
                             / \
                            x   T4
                           / \
                          T2  T3

        becomes
                            
                            |
                            x
                           / \
                          z    y
                         / \  / \
                        T1 T2 T3 T4
    
    zig:
        x does not have a grandparent, perform a single rotation

                            
                            y
                           / \
                          T1  x
                             / \
                            T2  T3

        becomes
                            x
                           / \
                          y   T3
                         / \
                        T1  T2


When to Splay:
    - When searching for key k:
        if k is found at position p:
            we splay p
        else:
            we splay the leaf position at which the search terminates unsuccesfully

    - When inserting key k:
        We splay the newly created internal node where k gets inserted

    - When deleting key k:
        We splay position p that is the parent of the removed node
        (recall that the removed node may be that originally containing k
         or a descendant node with replacement key)

Performance:
    the performance of Splay Tress for m insertions, deletions & searches
    is O(m log n)
"""

from treemap import TreeMap


class SplayTreeMap(TreeMap):
    """Sorted map implementation using a splay tree"""

    # ---- splay operation ----
    def _splay(self, p):
        while p != self.root():
            parent = self.parent(p)
            grand = self.parent(p)
            if grand is None:
                # zig case
                self._rotate(p)

            elif (parent == self.left(grand)) == (p == self.left(parent)):
                # zig-zig case
                self._rotate(parent)  # move parent up
                self._rotate(p)
            else:
                # zig-zag case
                self._rotate(p)  # move p up
                self._rotate(p)  # move p up again

    # ---- override balancing hooks ----
    def _rebalance_insert(self, p):
        self._splay(p)

    def _rebalance_delete(self, p):
        if p is not None:
            self._splay(p)

    def _rebalance_access(self, p):
        self._splay(p)
