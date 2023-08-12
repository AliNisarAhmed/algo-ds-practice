class Node:
    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def get(self, index):
        if self.head is None:
            return None
        current = self.head

        while current is not None and index > 0:
            current = current.next
            index -= 1

        return current

    def getTail(self):
        current = self.head
        while current is not None and current.next is not None:
            current = current.next

        return current

    def addAtHead(self, val):
        node = Node(val, self.head)
        self.head = node

    def addAtTail(self, val):
        if self.head is None:
            self.addAtHead(val)
            return

        tail = self.getTail()
        node = Node(val)
        tail.next = node

    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return
        prev = self.get(index - 1)
        if prev is None:
            return

        current = Node(val, prev.next)
        prev.next = current

    def deleteAtIndex(self, index):
        current = self.get(index)
        if current is None:
            return

        next = current.next

        if index == 0:
            self.head = next
        else:
            prev = self.get(index - 1)
            prev.next = next

    def print(self):
        current = self.head
        while current is not None:
            print(current.val)
            current = current.next


if __name__ == "__main__":
    l = LinkedList()
    l.addAtHead(1)
    l.addAtTail(3)
    l.addAtIndex(1, 2)
    l.print()
    print('----')
    l.deleteAtIndex(1)
    l.print()
