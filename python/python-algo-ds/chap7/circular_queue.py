class Empty(Exception):
    pass


class CircularQueue:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        head = self._tail._next
        return head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        old_head = self._tail._next
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = old_head._next
        self._size -= 1
        return old_head._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        head = self._tail._next

        if self.is_empty():
            newest._next = newest

        else:
            newest._next = head
            self._tail._next = newest

        self._tail = newest
        self._size += 1

    def rotate(self):
        if self._size > 0:
            # old head becomes the new tail
            self._tail = self._tail._next

    # R-7.5
    def size(self):
        # same as __len__ but without using _size prop
        if self._tail is None:
            return 0

        current = self._tail._next
        count = 1

        while current != self._tail:
            count += 1
            current = current._next

        return count

    # R-7.6
    def in_same_list(self, x, y):
        """Check if x and y are on same circular list"""
        walk = x._next

        while walk != x:
            if walk == y:
                return True
            walk = walk._next

        return False
