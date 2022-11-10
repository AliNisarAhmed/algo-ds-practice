from stack import ArrayStack
from queue import ArrayQueue


def subsets(items):
    s = ArrayStack()
    q = ArrayQueue()

    q.enqueue(set())

    for i in range(len(items)):
        s.push(items[i])

    while not s.is_empty():
        current = s.pop()
        print("current element", current)
        for i in range(len(q)):
            a = q.dequeue()
            print("a", a)
            q.enqueue(a)
            b = a | {current}
            q.enqueue(b)
            print("b", b)

    while not q.is_empty():
        x = q.dequeue()
        print("x", x)
