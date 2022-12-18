class Empty(Exception):
    pass


# 7.30
class LeakyStack:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self, capacity = 3):
        self._head = None
        self._size = 0
        self._capacity = capacity

    def __len__(self):
        return self._size

    def _at_capacity(self):
        return self._size == self._capacity

    def push(self, e):
        self._head = self._Node(e, self._head)
        if self._at_capacity():
            prev = self._head
            walk = self._head._next
            adv = self._head._next._next
            while adv is not None:
                prev = walk
                walk = adv
                adv = walk._next
            prev._next = None
        else:
            self._size += 1

    def print(self):
        walk = self._head
        while walk is not None:
            print(walk._element)
            walk = walk._next


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

# 7.24
class LinkedStackWithSentinel:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        newNode = self._Node(e, self._header._next)
        self._header._next = newNode

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")

        return self._header._next._element

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")

        removed = self._header._next
        self._header._next = removed._next

        return removed._element
