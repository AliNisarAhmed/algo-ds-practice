from queue import DeckQueue


class Empty(Exception):
    pass


class Full(Exception):
    pass


class StackUsingQueue:
    def __init__(self):
        self._data = DeckQueue()
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._data.is_empty()

    def push(self, v):
        # rotate the queue when pushing so that
        # when popping the order is correct
        self._data.enqueue(v)
        self._size += 1
        print('data before rotate', self._data._data)
        for _ in range(self._size - 1):
            self._data.enqueue(self._data.dequeue())
        print('data after rotate', self._data._data)

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        result = self._data.dequeue()
        self._size -= 1
        return result

    def top(self):
        return self._data.first()


class ArrayStack:
    def __init__(self, maxlen=None):
        # C-6.17
        self._data = [] if maxlen is None else [None] * maxlen
        self._size = 0
        # C-6.16
        self._maxlen = maxlen

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        if self._atCapacity():
            raise Full("Stack is full")
        if self._maxlen is None:
            self._data.append(e)
        else:
            self._data[self._size] = e
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        self._size -= 1
        return self._data.pop()

    def _atCapacity(self):
        if not self._maxlen:
            return False
        return self._size >= self._maxlen


# R-6.4
def remove_all_rec(S):
    if S.is_empty():
        return
    S.pop()
    remove_all_rec(S)


def reverse_list(ls):
    S = ArrayStack()
    for elem in ls:
        S.push(elem)
    for j in range(len(ls)):
        ls[j] = S.pop()
    return ls


# R-6.3
def transfer(S: ArrayStack, T: ArrayStack):
    """Transfer all elements of S to T"""
    while not S.is_empty():
        e = S.pop()
        T.push(e)


# R-6.1
# push(5) [5]
# push(3) [5, 3]
# pop()   [5]       => 3
# push(2) [5, 2]
# push(8) [5, 2, 8]
# pop() [5, 2]      => 8
# pop() [5]         => 2
# push(9) [5, 9]
# push(1) [5, 9, 1]
# pop() [5, 9]      => 1
# push(7) [5, 9, 7]
# push(6) [5, 9, 7, 6]
# pop() [5, 9, 7]   => 6
# pop() [5, 9]      => 7
# push(4) [5, 9, 4]
# pop() [5, 9]      => 4
# pop() [5]         => 9


# R-6.2
# 25 push - 10 pop + 3 errors = 18 (current size)

# C-6.15
# probability that m is highest of 3 values is 2/3
def get_max(S: ArrayStack):
    m = S.pop()
    if m < S.top():
        m = S.pop()
    return m

# C-6.18
# reverse a stack using transfer() function and two temp stacks


def rev_stack(S: ArrayStack):
    temp_stack_1 = ArrayStack()
    temp_stack_2 = ArrayStack()
    transfer(S, temp_stack_1)
    transfer(temp_stack_1, temp_stack_2)
    transfer(temp_stack_2, S)
    return S


# C-6.23
def store_T_below_S(R: ArrayStack, S: ArrayStack, T: ArrayStack):
    i = 0
    while not S.is_empty():
        R.push(S.pop())
        i += 1

    while not T.is_empty():
        S.push(T.pop())

    while i > 0:
        S.push(R.pop())
        i -= 1

    return S


if __name__ == "__main__":
    S = ArrayStack()
    T = ArrayStack()
    S.push(1)
    S.push(2)
    S.push(3)
    transfer(S, T)
    print(T.pop())
    print(T.pop())
    print(T.pop())

    # Reverse a list
    print('-----------------')
    ls = [1, 2, 3]
    print("Reverse a list")
    print(ls)
    reverse_list(ls)
    print(ls)
    print('-----------------')

    print("Reverse a stack with transfer")
    S = ArrayStack()
    S.push(1)
    S.push(2)
    S.push(3)
    print(S._data)
    S = rev_stack(S)
    print(S._data)
    print('-----------------')

    R = ArrayStack()
    R.push(1)
    R.push(2)
    R.push(3)

    S = ArrayStack()
    S.push(4)
    S.push(5)

    T = ArrayStack()
    T.push(6)
    T.push(7)
    T.push(8)
    T.push(9)

    print(S._data)
    S = store_T_below_S(R, S, T)
    print(S._data)
    print('-----------------')

    print("Stack using queue")
    S = StackUsingQueue()
    S.push(1)
    S.push(2)
    S.push(3)
    print(S.pop())
    print(S.pop())
    print(S.pop())
