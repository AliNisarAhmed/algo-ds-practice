from linked_list import LinkedList

def length(l: LinkedList):
    def length_rec(node):
        if node is None:
            return 0
        return 1 + length_rec(node._next)

    if l.is_empty():
        return 0

    return length_rec(l._head)


if __name__ == "__main__":
    l = LinkedList()
    l.add_first(3).add_first(2).add_first(1)
    print(length(l))
