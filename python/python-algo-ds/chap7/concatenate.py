from linked_list import LinkedList

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
