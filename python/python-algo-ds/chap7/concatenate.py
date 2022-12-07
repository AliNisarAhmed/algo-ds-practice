from linked_list import LinkedList
from doubly_linked_base import _DoublyLinkedBase

def concatenate(L: LinkedList, M: LinkedList):
    L._tail._next = M._head
    return L

if __name__ == "__main__":
    l = LinkedList()
    l.add_first(3).add_first(2).add_first(1)
    m = LinkedList()
    m.add_first(6).add_first(5).add_first(4)
    concatenate(l, m)
    l.print_list()

def concat(L: _DoublyLinkedBase, M: _DoublyLinkedBase):
    t1 = L._trailer._prev
    t2 = M._header._next

    t1._next = t2
    t2._prev = t1

    new_list = L
    new_list._trailer = M._trailer

    return new_list
