class Empty(Exception):
    pass


class LinkedQueue:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None  # front of the queue
        self._tail = None  # back of the queue
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1

    def rotate(self):
        """Rotate, i.e., the first element goes to the end"""
        if not self.is_empty():
            # send current head to after tail
            self._tail._next = self._head
            # set current head as the tail
            self._tail = self._head
            # set head to be the next of old head
            self._head = self._head._next
            # now remove the connection from the "old head" which is now at tail
            self._tail._next = None

    def concatenate(self, Q2):
        self._tail._next = Q2._head
        self._tail = Q2._tail
        self._size += Q2._size
        Q2._head = None
        Q2._tail = None
        Q2._size = 0

# 7.25


class LinkedQueueWithSentinel:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None)  # front of the queue
        self._tail = None  # back of the queue
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._header._next._element

    def dequeue(self):
        if self.is_empty():
            raise Empty("Queue is empty")
        answer = self._header._next
        self._header._next = answer._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer._element

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._header._next = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1
