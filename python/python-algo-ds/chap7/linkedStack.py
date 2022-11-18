class Empty(Exception):
    pass


class LinkedStack:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self.__element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self.size == 0

    def push(self, e):
        self._head = self._Node(e, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")

        return self._head.element

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        result = self._head._element
        self._head = self._head.next
        self._size -= 1
        return result
