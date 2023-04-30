class Empty(Exception):
    pass


# C-7.30
class LeakyStack:

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self, capacity=3):
        self._head = None
        self._tail = None
        self._size = 0
        self._capacity = capacity

    def __len__(self):
        return self._size

    def _at_capacity(self):
        return self._size >= self._capacity

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        new_node = self._Node(e, None)
        if self.is_empty():
            self._head = new_node
            self._tail = new_node
            self._size += 1
        else:
            self._tail._next = new_node
            self._tail = new_node

            if self._at_capacity():
                self._head = self._head._next
            else:
                self._size += 1

        return self

    def pop(self):
        if self.is_empty():
            return None

        prev = None
        walk = self._head

        while walk is not self._tail:
            prev = walk
            walk = walk._next

        popped = self._tail

        if prev is None:
            # if prev is None, that means only 1 element in stack
            self._tail = None
            self._head = None
        else:
            prev._next = None
            self._tail = prev

        self._size -= 1
        return popped._element

    def print(self):
        walk = self._head
        while walk is not None:
            print(walk._element)
            walk = walk._next


# C-7.24
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

        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        result = self._head._element
        self._head = self._head._next
        self._size -= 1
        return result


# C-7.24
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


if __name__ == "__main__":
    print('---- 7.30 ----')
    ls = LeakyStack()
    ls.push(1)
    ls.push(2)
    ls.push(3)
    ls.push(4)

    ls.print()

    print(ls.pop())
    print(ls.pop())
    print(ls.pop())
    print(ls.pop())

    ls.push(1)
    ls.push(2)
    ls.push(3)
    ls.push(4)

    ls.print()
    print('--------')
