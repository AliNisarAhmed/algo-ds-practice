from linked_binary_tree import LinkedBinaryTree
from euler_tour import EulerTour


def preorder_indent(T, p, d):
    """
    d is the depth of Position p in the Tree T

    printing table of content is preorder traversal
    """
    print(2 * d * " " + str(p.element()))
    for c in T.children(p):
        preorder_indent(T, c, d + 1)


def preorder_label(T, p, d=0, path=[]):
    """
    In the above function, we assume the labels for the table of content are provided
    This function generates the labels based on the depth in the tree
    """
    label = ".".join(str(j + 1) for j in path)
    s = 2 * d * " " + label
    if d > 0:
        s += "."
    print(s, p.element())
    path.append(0)
    for c in T.children(p):
        preorder_label(T, c, d + 1, path)
        path[-1] += 1
    path.pop()


class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        print(2 * d * " " + str(p.element()))


class PreorderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self, p, d, path):
        label = ".".join(str(j + 1) for j in path)
        print(2 * d * " " + label, p.element())


if __name__ == "__main__":
    t = LinkedBinaryTree()
    root = t._add_root("abc")
    left = t._add_left(root, "def")
    right = t._add_right(root, "ghi")
    t._add_left(left, "jkl")
    right2 = t._add_right(left, "mno")
    t._add_left(right, "pqr")
    right3 = t._add_right(right, "stu")
    t._add_left(right2, "vwx")

    preorder_label(t, root)

    print(f"left leaves count: {t.count_left_leaves()}")

    tour = PreorderPrintIndentedTour(t)
    tour.execute()

    labeled_tour = PreorderPrintIndentedLabeledTour(t)
    labeled_tour.execute()
