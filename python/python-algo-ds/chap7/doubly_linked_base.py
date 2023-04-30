class _DoublyLinkedBase:

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, e, prev, next):
            self._element = e
            self._prev = prev
            self._next = next

    def __init__(self):
        # header and trailers are "sentinel" nodes
        # which greatly simplify the underlying logic
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """add element e between two existing nodes and return new node"""
        newest = self._Node(e, predecessor, successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """delete non sentinal node from the list and return its element"""
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        # record deleted element
        element = node._element
        # deprecate node
        node._prev = node._next = node._element = None

        return element

    # R-7.8
    def middle(self):
        if self._size == 0:
            raise ValueError("List is empty")
        left = self._header._next
        right = self._trailer._prev

        while left != right and left._next != right:
            left = left._next
            right = right._prev

        return left

    # C-7.33
    def reverse(self):
        prev = self._header
        walk = self._header._next
        while walk is not None:
            adv = walk._next
            walk._next = prev
            walk._prev = adv
            prev = walk
            walk = adv
        self._header, self._trailer = self._trailer, self._header
