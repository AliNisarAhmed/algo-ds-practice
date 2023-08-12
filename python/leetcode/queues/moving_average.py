from circular_queue import MyCircularQueue


class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.q = [0] * size
        self.head = self.window_sum = 0
        self.count = 0
        self.queue = MyCircularQueue(size)

    def next(self, val: int) -> float:
        self.count += 1
        tail = (self.head + 1) % self.size
        self.window_sum = self.window_sum - self.q[tail] + val
        self.head = (self.head + 1) % self.size
        self.q[self.head] = val

        return self.window_sum / min(self.size, self.count)

    def next2(self, val: int) -> float:
        self.count += 1
        if self.queue.isEmpty():
            self.queue.enQueue(val)
            self.window_sum = val
        else:
            self.window_sum = self.window_sum + val

            if self.queue.isFull():
                self.window_sum -= self.queue.Front()
                self.queue.deQueue()

            self.queue.enQueue(val)

        return self.window_sum / min(self.count, self.size)


if __name__ == "__main__":
    m = MovingAverage(5)
    print(m.next2(1))
    print(m.next2(2))
    print(m.next2(3))
    print(m.next2(4))
    print(m.next2(5))
    print(m.next2(6))
    print(m.next2(7))

    print('----')

    m = MovingAverage(5)
    print(m.next(1))
    print(m.next(2))
    print(m.next(3))
    print(m.next(4))
    print(m.next(5))
    print(m.next(6))
    print(m.next(7))
