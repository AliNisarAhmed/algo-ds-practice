

class MyQueue:

    def __init__(self):
        self.back = []
        self.front = []

    def push(self, x):
        self.back.append(x)

    def pop(self):
        if self.empty():
            return None

        if len(self.front) == 0:
            while len(self.back) > 0:
                self.front.append(self.back.pop())

        return self.front.pop()

    def peek(self):
        if len(self.front) > 0:
            return self.front[-1]

        return self.back[0]

    def empty(self):
        return len(self.back) == 0 and len(self.front) == 0


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    print(q.peek())
    print(q.pop())
    print(q.empty())
