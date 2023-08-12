class MyCircularQueue:
    def __init__(self, k=10):
        self.size = k
        self.head = None
        self.tail = None
        self.data = [None] * k

    def enQueue(self, value):
        if self.isFull():
            return False

        if self.isEmpty():
            self.head = 0

        self.tail = 0 if self.isEmpty() else ((self.tail + 1) % self.size)
        self.data[self.tail] = value
        return True

    def deQueue(self):
        if self.isEmpty():
            return False

        self.data[self.head] = None

        self.head = (self.head + 1) % self.size

        if self.data[self.head] is None:
            self.head = None
            self.tail = None

        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.data[self.tail]

    def isEmpty(self) -> bool:
        return self.head is None or self.tail is None

    def isFull(self) -> bool:
        if self.isEmpty():
            return False

        return (self.tail + 1) % self.size == self.head


if __name__ == "__main__":
    c = MyCircularQueue(5)
    print(c.enQueue(1))
    print(c.data)
    print(c.enQueue(2))
    print(c.data)
    print(c.enQueue(3))
    print(c.data)
    print(c.enQueue(4))
    print(c.data)
    print(c.enQueue(5))
    print(c.data)
    print('head: ', c.head)
    print('tail: ', c.tail)
    print('is full: ', c.isFull())
    print('is empty: ', c.isEmpty())

    print('----------------------')
    print(c.deQueue())
    print(c.data)
    print(c.deQueue())
    print(c.data)
    print(c.deQueue())
    print(c.data)
    print(c.deQueue())
    print(c.data)
    print(c.deQueue())
    print(c.data)
    print('is full: ', c.isFull())
    print('is empty: ', c.isEmpty())
