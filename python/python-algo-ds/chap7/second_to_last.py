from linked_list import LinkedList 

class Empty(Exception):
    pass

def second_to_last(L: LinkedList):
    if L.is_empty():
        raise Empty("List is empty")

    current = L._head
    next = current._next

    if next is None:
        raise Empty("List has single element")

    next_to_next = next._next

    while next_to_next is not None:
        current = next
        next = next_to_next
        next_to_next = next_to_next._next

    return current._element

if __name__ == "__main__":
    l = LinkedList()
    l.add_first(1)
    l.add_last(2)
    l.add_last(3)

    l.print_list()

    res = second_to_last(l)

    print(res)
    print(res == 2)
