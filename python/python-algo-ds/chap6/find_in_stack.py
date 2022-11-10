# check if a value is in stack using a Queue and a constant
# number of variables
# Stack order should not change

from stack import ArrayStack
from queue import ArrayQueue


def find_in_stack(s: ArrayStack, v):
    q = ArrayQueue()
    found = False

    while not s.is_empty():
        current = s.pop()
        if current == v:
            # do not return if the element is found
            # Just dump the whole stack in the queue
            # since the algo is O(n) anyways
            found = True
        q.enqueue(current)

    move_queue_to_stack(s, q)

    return found


def move_queue_to_stack(s: ArrayStack, q: ArrayQueue):
    while not q.is_empty():
        s.push(q.dequeue())
