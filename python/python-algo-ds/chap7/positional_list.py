from .doubly_linked_base import _DoublyLinkedBase


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

        # R-10.7
        def __hash__(self):
            return hash(self.element())

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

    # R-7.15
    def __reversed__(self):
        cursor = self.last()
        while cursor is not None:
            yield cursor.element()
            cursor = self.before(cursor)

    def print_list(self):
        for e in self:
            print('Element: ', e)

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

    # R-7.12
    def max(self):
        if self.is_empty():
            return None

        result = self.first().element()
        for e in self:
            if e > result:
                result = e
        return result

    # R-7.13
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

    # R-7.14
    def find_rec(self, e):
        return self._find_rec(e, self.first())

    # R-7.16
    def add_last2(self, e):
        """
        Using only {is_empty, first, last, prev, next, add_after, add_first}
        """
        if self.is_empty():
            return self.add_first(e)

        return self.add_after(self.last(), e)

    def add_before2(self, p, e):
        """
        Using only {is_empty, first, last, prev, next, add_after, add_first}
        """
        if p == self.first():
            return self.add_first(e)
        else:
            return self.add_after(self.before(p), e)

    # R-7.17
    def move_to_front(self, p):
        # node has a _prev and a _next
        node = self._validate(p)
        # if node is not already the first node
        if node != self._header._next:
            # remove node from existing location
            node._prev._next = node._next
            node._next._prev = node._prev
            # make node point to its new neighbours
            node._prev = self._header
            node._next = self._header._next
            # make new neighbours point to node
            node._prev._next = node
            node._next._prev = node

    # C-7.34
    def swap(self, p, q):
        p_val = p.element()
        q_val = q.element()
        p._node._element = q_val
        q._node._element = p_val

    # C-7.38
    def bubble_sort(self):
        didSwap = True

        while didSwap:
            walk = self.first()
            didSwap = False
            while walk is not None:
                next_pos = self.after(walk)
                if next_pos is not None and next_pos.element() < walk.element():
                    self.swap(walk, next_pos)
                    if not didSwap:
                        didSwap = True
                walk = next_pos

            if not didSwap:
                break


# C-7.37
def two_sum(pl: PositionalList, v):
    """pl is sorted"""
    if pl.is_empty():
        return (None, None)

    start = pl.first()
    end = pl.last()

    while start is not end:
        total = start.element() + end.element()
        print('total', total)
        if total == v:
            return start, end
        elif total < v:
            start = pl.after(start)
            if start == end:
                break
        else:
            end = pl.before(end)
            if start == end:
                break

    return None, None


if __name__ == "__main__":
    pl = PositionalList()
    one = pl.add_first(1)
    two = pl.add_after(one, 2)
    three = pl.add_after(two, 3)
    four = pl.add_after(three, 42)

    pl.print_list()
    # pl.swap(two, three)
    pl.print_list()

    print('--------')
    print('---- 7.37 ----')

    p1, p2 = two_sum(pl, 84)
    print(p1.element() if p1 is not None else p1)
    print(p2.element() if p2 is not None else p2)

    print('--------')
    print('---- 7.38 ----')

    pl = PositionalList()
    pl.add_first(1)
    two = pl.add_first(2)
    pl.add_last(4)
    pl.add_last(3)
    pl.add_last(10)
    pl.add_after(two, 100)

    pl.print_list()
    pl.bubble_sort()
    pl.print_list()

# R-7.18
# List: {a, b, c, d, e, f}
# sequence of access: (a, b, c, d, e, f, a, c, f, b, d, e)

# a -> a, b, c, d, e, f
# b -> b, a, c, d, e, f
# c -> c, b, a, d, e, f
# d -> d, c, b, a, e, f
# e -> e, d, c, b, a, f
# f -> f, e, d, c, b, a
# a -> a, f, e, d, c, b
# c -> c, a, f, e, d, b
# f -> f, c, a, e, d, b
# b -> b, f, c, a, e, d
# d -> d, b, f, c, a, e
# e -> e, d, b, f, c, a

# 7.19
# Minimum is 0 elements with access less than k
# this is because we can access each element k times, thus ZERO elements
# accessed fewer than k times
# Maximum is n - 1 elements
# since we can access one element kn times
# leaving others with 0 accesses
# thus the number of elements with <k accesses = n - 1
