from linked_list import LinkedList, Node
import unittest


class MyLinkedList(LinkedList):
    def partition(self, data):
        if self.head is None:
            return
        if self.head.next is None:
            return

        count, tail = self.tail(data)
        current = self.head

        while count > 1 and current is not None:
            if current.data >= data:
                new_tail = Node(current.data, current.next)
                if current.next is not None:
                    current.data = current.next.data
                    current.next = current.next.next
                tail.next = new_tail
                new_tail.next = None
                tail = new_tail
                count -= 1
            else:
                current = current.next

        return self

    def tail(self, data):
        count = 0
        current = self.head
        while current.next is not None:
            if current.data >= data:
                count += 1
            current = current.next

        return count, current


class TestPartition(unittest.TestCase):

    def test_partition(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        linked_list.partition(10)
        self.assertEqual(linked_list.get_all_data(), [])

        print('Test: One element list, left list empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(0)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: Right list is empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(10)
        self.assertEqual(linked_list.get_all_data(), [5])

        print('Test: General case')
        # Partition = 10
        # Input: 4, 3, 13, 8, 10, 1, 14, 10, 12
        # Output: 4, 3, 8, 1, 10, 10, 13, 14, 12
        linked_list = MyLinkedList(Node(12))
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(14)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(8)
        linked_list.insert_to_front(13)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(4)
        partitioned_list = linked_list.partition(10)
        self.assertEqual(partitioned_list.get_all_data(),
                         [4, 3, 8, 1, 10, 12, 13, 10, 14])

        print('Success: test_partition')


def main():
    test = TestPartition()
    test.test_partition()


if __name__ == '__main__':
    main()
