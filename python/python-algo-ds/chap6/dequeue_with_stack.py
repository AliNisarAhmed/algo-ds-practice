from stack import ArrayStack

# C-6.26


class DequeueWithTwoStack:

    def __init__(self) -> None:
        self.front = ArrayStack()
        self.back = ArrayStack()

    def add_first(self, v):
        self.front.push(v)
        return self

    def add_last(self, v):
        self.back.push(v)
        return self

    def delete_first(self):
        if self.front.is_empty():
            self._move_back_to_front()
        res = self.front.pop()
        print('delete_first', res)
        return self

    def delete_last(self):
        if self.back.is_empty():
            self._move_front_to_back()
        res = self.back.pop()
        print('delete_last', res)
        return self

    def first(self):
        t = self.front.top()
        print('first: ', t)
        return self

    def last(self):
        t = self.back.top()
        print('last: ', t)
        return self

    def is_empty(self):
        return self.front.is_empty() and self.back.is_empty()

    def __len__(self):
        return len(self.front) + len(self.back)

    def _move_back_to_front(self):
        while not self.back.is_empty():
            self.front.push(self.back.pop())

    def _move_front_to_back(self):
        while not self.front.is_empty():
            self.back.push(self.front.pop())

# add_first(4)    [4]
# add_last(8)     [4, 8]
# add_last(9)     [4, 8, 9]
# add_first(5)    [5, 4, 8, 9]
# back()                              => 9
# delete_first()  [4, 8, 9]           => 5
# delete_last()   [4, 8]              => 9
# add_last(7)     [4, 8, 7]
# first()                             => 4
# last()                              => 7
# add_last(6)     [4, 8, 7, 6]
# delete_first()  [8, 7, 6]           => 4
# delete_first()  [7, 6]              => 8


if __name__ == "__main__":
    q = DequeueWithTwoStack()
    q.add_first(4)
    q.add_last(8)
    q.add_last(9)
    q.add_first(5)
    # print(q.front._data, q.back._data)
    q.last()
    # print(q.front._data, q.back._data)
    q.delete_first()
    q.delete_last()
    q.add_last(7)
    q.first()
    q.last()
    q.add_last(6)
    q.delete_first()
    q.delete_first()
