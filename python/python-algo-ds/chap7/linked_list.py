class Empty(Exception):
    pass 

class LinkedList:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def add_first(self, e):
        newest = self._Node(e, None)
        newest._next = self._head
        self._head = newest

        if self.is_empty():
            self._tail = newest

        self._size += 1
        return self

    def add_last(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._tail = newest
            self._head = newest
            return self

        self._tail._next = newest
        self._tail = newest
        self._size += 1
        return self

    def remove_first(self):
        if self.is_empty():
            raise Empty("List is empty")
        removed = self._head
        self._head = self._head._next
        self._size -= 1
        return removed._element

    def print_list(self):
        current = self._head
        while current is not None:
            print(f"{current._element}")
            current = current._next

