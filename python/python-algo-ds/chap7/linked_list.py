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

    def reverse(self):
        prev = None
        walk = self._head
        while walk is not None:
            adv = walk._next
            walk._next = prev
            prev = walk
            walk = adv
        self._head = prev


# 7.27
class LinkedListRecursive:
    # class _Node:
    #     __slots__ = '_element', '_next'
    #
    #     def __init__(self, element, next):
    #         self._element = element
    #         self._next = next
    #
    def __init__(self, element = None):
        self._head = element
        self._rest = None
        self._size = 0

    def is_empty(self):
        return self._head is None 

    def __len__(self):
        return self._size

    def add_first(self, e):
        if self._head is None:
            self._head = e
            self._size += 1
        else:
            current = self._head
            self._head = e
            self._size += 1
            if self._rest is None:
                self._rest = LinkedListRecursive(current)
            else:
                self._rest.add_first(current)

    def add_last(self, e):
        self._size += 1
        if self._head is None:
            self._head = e
        else:
            if self._rest is None:
               self._rest = LinkedListRecursive(e) 
            else:
                self._rest.add_last(e)

    def remove_first(self):
        if self._head is None:
            return None
        else:
            self._size -= 1
            if self._rest is None:
                removed = self._head
                self._head = None
                return removed
            else:
                removed = self._head
                self._head = self._rest._head
                self._rest = self._rest._rest

    def print_list(self):
        if self._head is not None:
            print(self._head)
            if self._rest is not None:
                self._rest.print_list()


def reverse(head):
    if head is None:
        return head
    if head._next is None:
        return head

    new_head = reverse(head._next)
    head._next._next = head
    head._next = None

    return new_head
