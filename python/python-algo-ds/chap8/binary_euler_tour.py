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


if __name__ == "__main__":
    t = MutableLinkedBinaryTree()
    root = t.add_root("a")
    b = t.add_left(root, "b")
    c = t.add_right(root, "c")
    d = t.add_left(b, "d")
    e = t.add_right(b, "e")
    f = t.add_left(c, "f")
    g = t.add_right(c, "g")

    t.add_left(d, "h")
    t.add_right(d, "h")
    t.add_left(e, "h")
    t.add_right(e, "h")
    t.add_left(f, "h")
    t.add_right(f, "h")
    t.add_left(g, "h")
    t.add_right(g, "h")

    tour = LevelNumberEulerTour(t)

    tour.execute()
