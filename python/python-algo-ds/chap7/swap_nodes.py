# Singly Linked List
def swap_nodes(x, y):
    temp = y._next
    y._next = x
    x._next = y

    # Plus, we need reference to x's previous node as well

    # Compared to above, swap nodes in Doubly linked List will be easier


    
