
from stack import ArrayStack, Empty


# C-6.25
class QueueWithTwoStack:
    def __init__(self):
        # enqueing stack
        self.e_stack = ArrayStack()
        # dequeuing stack
        self.d_stack = ArrayStack()

    def __len__(self):
        return len(self.e_stack) + len(self.d_stack)

    def is_empty(self):
        return len(self.e_stack) == 0 and len(self.d_stack) == 0

    def dequeue(self):
        if len(self.d_stack) == 0:
            if len(self.e_stack) == 0:
                raise Empty('Queue is empty')
            self._transfer()

        return self.d_stack.pop()

    def enqueue(self, v):
        self.e_stack.push(v)

    def first(self):
        if len(self.d_stack) == 0:
            if len(self.e_stack) == 0:
                raise Empty('Queue is empty')
            self._transfer()

        return self.d_stack.top()

    def _transfer(self):
        while not self.e_stack.is_empty():
            self.d_stack.push(self.e_stack.pop())
