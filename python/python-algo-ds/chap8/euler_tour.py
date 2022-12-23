"""
The Euler tour traversal of a general tree T can be informally defined as a 
"Walk" around T, where we start going from the root toward its leftmost child,
viweing the edges of T as being walls that we always keep to the left.
    kinda like postorder traversal, but we do not skip any nodes while doing postorder

Thus, we visit each root node twice, once on the way down to the left tree and then 
once on the way up to the right tree
"""


class EulerTour:
    """
    Abstract base class for performing Euler tour of a tree

    _hook_previsit and _hook_postvisit may be overridden by subclasses
    """

    def __init__(self, tree):
        self._tree = tree

    def tree(self):
        return self._tree

    def execute(self):
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, [])

    def _tour(self, p, d, path):
        """
        Perform tour of subtree rooted at Position P

        p       = Position of current node being visited
        d       = depth of p in the tree
        path    = list of indices of children on path from root to p
        """

        self._hook_previsit(p, d, path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tour(c, d + 1, path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p, d, path, results)
        return answer

    def _hook_previsit(self, p, d, path):
        """
        This function is called once for each position, immediately before its subtrees
        (if any) are traversed.

        Parameter p is a position in the tree
        d is the depth of that position
        and path is a list of indices

        No return value is expected from this function
        """
        pass

    def _hook_postvisit(self, p, d, path, results):
        """
        This function is called once for each position, immediately after its subtrees
        (if any) are traversed.

        The fist 3 params are the same as above,
        The last parameter is a list of objects that were provided as return values from
        the post visits of the respective subtrees of p.

        Any value returned by this call will be available to the parent of p during its postvisit
        """
        pass
