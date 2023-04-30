class _SingleLinkedBase:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, e, next):
            self._element = e
            self._next = next

    def __init__(self):
        # header and trailers are "sentinel" nodes
        # which greatly simplify the underlying logic
        self._header = self._Node(None, None)
        self._trailer = self._Node(None, None)
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """add element e between two existing nodes and return new node"""
        newest = self._Node(e, successor)
        predecessor._next = newest
        self._size += 1
        return newest

    def _insert_before(self, e, succ):
        prev = self._find_prev(succ)
        return self._insert_between(e, prev, succ)

    def _find_prev(self, node):
        if node is self._header or node is self._header._next:
            return None
        prev = self._header
        walk = self._header._next

        while walk is not node:
            prev = walk
            walk = walk._next

        return prev

    def _delete_node(self, node):
        """delete non sentinal node from the list and return its element"""
        prev = self._header
        walk = self._header._next

        while walk is not node and walk is not None:
            prev = walk
            walk = walk._next

        prev._next = node._next
        node._next = None
        self._size -= 1
        return node._element
