from binary_euler_tour import BinaryEulerTour


class BinaryLayout(BinaryEulerTour):
    """
    computes theh graphihcal layout of a binary tree

    The geometry is determined by the algo that assigns
    x and y coordinates to each position using the following two rules

    1. x(p) is the number of positions visited before p in an inorder traversal of T
    2. y(p) is the depth of p in T

    Note: origin is the upper left corner of the screen
    """

    def __init__(self, tree):
        super().__init__(tree)
        self._count = 0  # initialized count of process nodes

    def _hook_invisit(self, p, d, path):
        p.element().setX(self._count)  # x-coordinate serialized by count
        p.element().setY(d)  # y coordinate is the depth
        self._count += 1  # advance count of processed node
