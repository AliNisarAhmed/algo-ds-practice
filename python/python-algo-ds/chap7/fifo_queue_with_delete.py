from positional_list import PositionalList

# C-7.39
class FifoQWithDel:

    def __init__(self):
        self._data = PositionalList()

    def enqueue(self, e):
        return self._data.add_last(e)

    def dequeue(self):
        return self._data.delete(self._data.first())

    def delete(self, p):
        return self._data.delete(p)

    def print_list(self):
        return self._data.print_list()


if __name__ == "__main__":
    fq = FifoQWithDel()
    fq.enqueue(1)
    two = fq.enqueue(2)
    fq.enqueue(3)
    print(fq.dequeue())
    fq.enqueue(4)
    fq.delete(two)
    fq.print_list()
    print(fq.dequeue())
    print(fq.dequeue())
