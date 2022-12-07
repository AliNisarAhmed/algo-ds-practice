from doubly_linked_base import _DoublyLinkedBase


class PositionalList(_DoublyLinkedBase):
    """
    A sequential container of elements, a linked list which allows positional access
    """
    class Position:
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
        if p._node._next is None:
            raise ValueError("p is not longer valid")
        return p._node

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    # --------------------- ACCESSORS -----------------------------------

    def first(self):
        return self._make_position(self._header._next)

    def last(self):
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """return the position just before position p"""
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list"""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def __reversed__(self):
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

    # --------------------- MUTATORS -----------------------------------

    # override inherited version to return Position instead of Node
    def _insert_between(self, e, pred, succ):
        node = super()._insert_between(e, pred, succ)
        return self._make_position(node)

    def add_first(self, e):
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element

    def replace(self, p, e):
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value

    def max(self):
        if self.is_empty():
            return None

        result = self.first().element()
        for e in self:
            if e > result:
                result = e
        return result

    def find(self, e):
        for element in self:
            if element == e:
                return self._make_position(e)
        return None

    def _find_rec(self, e, node):
        if node is self._trailer:
            return None
        elif node.element() == e:
            return node
        else:
            return self._find_rec(e, node._next)

    def find_rec(self, e):
        return self._find_rec(e, self.first())

    def add_last2(self, e):
        """
        Using only {is_empty, first, last, prev, next, add_after, add_first}
        """
        if self.is_empty():
            self.add_first(e)
            return self

        self.add_after(self.last(), e)
        return self

    def add_before2(self, p, e):
        """
        Using only {is_empty, first, last, prev, next, add_after, add_first}
        """
        if p == self.first():
            return self.add_first(e)
        else:
            return self.add_after(self.before(p), e)
