class Solution:

    def remove_nth_from_end(self, head, n):
        if head is None:
            return

        ptr, length = head, 0

        while ptr is not None:
            ptr, length = ptr.next, length + 1

        if length == n:
            return head.next

        ptr = head

        for i in range(1, length - n):
            ptr = ptr.next

        ptr.next = ptr.next.next

        return head

