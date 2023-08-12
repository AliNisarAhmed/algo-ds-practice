from linked_list_leedcode import Node


class Solution:
    def reverse(head):
        if head is None:
            return head

        current = head

        while current.next is not None:
            first = current.next
            second = first.next

            first.next = head
            current.next = second
            head = first

        return head

    def print(head):
        current = head
        while current is not None:
            print(current.val)
            print("->")
            current = current.next


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2, Node(3))

    Solution.print(head)
    new_head = Solution.reverse(head)
    Solution.print(new_head)
