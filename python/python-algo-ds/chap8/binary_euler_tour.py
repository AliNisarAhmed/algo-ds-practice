from euler_tour import EulerTour
from linked_binary_tree import MutableLinkedBinaryTree


class BinaryEulerTour(EulerTour):
    """
    Abtract base class for performing Euler tour of a binary tree

    This version includes an additional _hook_invisit that is called after the tour
    of the left subtree (if any), yet before the tour of the right subtree (if any)

    Note: Right child is always assigned index 1 in path, even if no left sibling
    """

    def _tour(self, p, d, path):
        results = [None, None]  # will update with results of recursion

        self._hook_previsit(p, d, path)  # pre-visit for p

        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tour(self._tree.left(p), d + 1, path)
            path.pop()

        self._hook_invisit(p, d, path)  # in visit for p

        if self._tree.right(p) is not None:
            path.append(1)  # See note in docstring
            results[1] = self._tour(self._tree.right(p), d + 1, path)
            path.pop()

        answer = self._hook_postvisit(p, d, path, results)

        return answer

    def _hook_invisit(self, p, d, path):
        """
        To be overriden
        """
        pass


# R-8.17
class LevelNumberEulerTour(BinaryEulerTour):
    def _tour(self, p, d, path, level=0):
        if self._tree.left(p) is not None:
            self._tour(self._tree.left(p), d + 1, path, 2 * level + 1)

        if self._tree.right(p) is not None:
            self._tour(self._tree.right(p), d + 1, path, 2 * level + 2)
        print(level)


# C-8.47
# Balance factor for an internal position of a proper binary tree
# = difference b/w heights of the right and left subtrees
class BalanceFactor(BinaryEulerTour):
    def _hook_previsit(self, p, d, path):
        p.set_height(0)

    def _hook_postvisit(self, p, d, path, results):
        balance = 0
        tree = self.tree()
        if not tree.is_leaf(p):
            left_child = tree.left(p)
            right_child = tree.right(p)

            if left_child._height > right_child._height:
                p.set_height(left_child._height + 1)
            else:
                p.set_height(right_child._height + 1)
            balance = abs(right_child._height - left_child._height)

        print(balance)


# C-8.48
# Let
# rank   = when a vertex is visited during traversal, e.g. first element visited has rank 1
# pre    = rank of a position during pre-order
# post   = rank of a position during post-order
# d      = depth of a position
# desc   = number of descendants of a position including p
# Derive a formula for post in terms of pre, desc, and d
# Answer:
# post = pre + d + desc - 1


if __name__ == "__main__":
    t = MutableLinkedBinaryTree()
    root = t.add_root("a")
    b = t.add_left(root, "b")
    c = t.add_right(root, "c")
    d = t.add_left(b, "d")
    e = t.add_right(b, "e")
    f = t.add_left(c, "f")
    g = t.add_right(c, "g")

    t.add_left(d, "l1")
    t.add_right(d, "l2")
    t.add_left(e, "l3")
    t.add_right(e, "l4")
    t.add_left(f, "l5")
    t.add_right(f, "l6")
    t.add_left(g, "l7")
    t.add_right(g, "l8")

    # tour = LevelNumberEulerTour(t)

    # tour.execute()

    balance_factor = BalanceFactor(t)

    balance_factor.execute()
