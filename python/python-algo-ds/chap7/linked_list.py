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
        else:
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
            print("element: ", f"{current._element}")
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

    # R-7.1
    def second_to_last(self):
        if self.is_empty():
            raise Empty("List is empty")

        if self._size == 1:
            return None

        walk = self._head
        last = self._head._next

        while last._element != self._tail._element:
            walk = last
            last = last._next

        return walk._element

    # R-7.3
    def count(self):
        return self._count(self._head, 0)

    def _count(self, node, current_count):
        if self.is_empty() or node is None:
            return current_count

        return self._count(node._next, current_count + 1)


# R-7.2
def join_lists(node1, node2):
    """
    node1 and node2 are the first nodes of two lists
    """

    walk = node1
    last = node1._next
    while last is not None:
        walk = last
        last = last._next

    walk._next = node2

    return node1

# 7.27


class LinkedListRecursive:
    # class _Node:
    #     __slots__ = '_element', '_next'
    #
    #     def __init__(self, element, next):
    #         self._element = element
    #         self._next = next
    #
    def __init__(self, element=None):
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


if __name__ == "__main__":
    print("---- 7.1 ----")
    linkL = LinkedList()
    linkL.add_first(1).add_first(2).add_first(3).add_first(4)

    print(linkL._size)

    linkL.print_list()

    print("Second to last: ", linkL.second_to_last())

    print('------------')

    print('---- 7.2 ----')

    l1 = LinkedList()
    l1.add_last(1)
    l1.add_last(2)
    l1.add_last(3)

    l2 = LinkedList()
    l2.add_last(6)
    l2.add_last(5)
    l2.add_last(4)

    join_lists(l1._head, l2._head)

    l1.print_list()

    print('--------')

    print('---- 7.3 ----')

    l3 = LinkedList()
    l3.add_last(3)
    l3.add_last(3)
    l3.add_last(3)
    l3.add_last(3)
    l3.add_last(3)

    print(l3.count())

    print('--------')
