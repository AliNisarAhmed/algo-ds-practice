from single_linked_base import _SingleLinkedBase


class ForwardList(_SingleLinkedBase):

    class Position():
        def __init__(self, container, node):
            """
            this constructor is private, use _make_position
            node is the Node class from _DoublyLinkedBase
            container is the "self" of the class creating this Position
            """
            self._container = container
            self._node = node

        def element(self):
            return self._node._element

        def __eq__(self, other):
            """Return True if other is a Position representing the same location"""
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            return not (self == other)

    # --------------------- UTILITY METHODS -----------------------------------
    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid"""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:  # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)  # self passed as container

    def _insert_between(self, e, pred, succ):
        node = super()._insert_between(e, pred, succ)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer, None)

    def print(self):
        if self.is_empty():
            print('List empty')
            return

        walk = self._header._next
        while walk is not None:
            print('element: ', walk._element)
            walk = walk._next


if __name__ == "__main__":
    fl = ForwardList()
    fl.add_first(1)
    fl.add_first(2)
    fl.add_first(3)
    fl.print()
