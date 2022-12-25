from euler_tour import EulerTour
from linked_binary_tree import LinkedBinaryTree


def parenthesize(T, p):
    """
    Produces a parenthetic string representation of a tree
    e.g: 1 (2, 3, (4, 5, 6))

    essentially a preorder traversal, but we need to print '(' and ')' at the right time
    hence we cannot use the generic function
    """
    print(p.element(), end="")  # use of end avoids trailing newline
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = " (" if first_time else ", "
            print(sep, end="")
            first_time = False
            parenthesize(T, c)
        print(")", end="")


class ParenthesizeTour(EulerTour):
    def _hook_previsit(self, p, d, path):

        if path and path[-1] > 0:  # p follows a sibling (first sibling has path = 0)
            print(", ", end="")  # so preface with a comma

        print(p.element(), end="")  # then print element

        if not self.tree().is_leaf(p):  # if p has children
            print(" (", end="")  # print opening parenthesis

    def _hook_postvisit(self, p, d, path, results):
        if not self.tree().is_leaf(p):
            print(")", end="")


if __name__ == "__main__":

    t = LinkedBinaryTree()
    root = t._add_root("abc")
    left = t._add_left(root, "def")
    right = t._add_right(root, "ghi")
    t._add_left(left, "jkl")
    t._add_right(left, "mno")
    t._add_left(right, "pqr")
    t._add_right(right, "stu")

    tour = ParenthesizeTour(t)
    tour.execute()