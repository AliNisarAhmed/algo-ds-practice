# Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

# The first node is considered odd, and the second node is even, and so on.

from linked_list_leedcode import Node


class Solution:
    def oddEvenList(self, head):
        if head is None:
            return head

        odds = Node(0)
        evens = Node(0)
        oddsHead = odds
        evensHead = evens
        isOdd = True

        while head:
            if isOdd:
                odds.next = head
                odds = odds.next
            else:
                evens.next = evens
                evens = evens.next

            isOdd = not isOdd
            head = head.next

        evens.next = None
        odds.next = evensHead.next

        return oddsHead.next
