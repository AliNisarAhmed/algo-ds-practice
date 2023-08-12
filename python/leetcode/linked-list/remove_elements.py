class Solution:
    def removeElements(self, head, val):
        if head is None:
            return head

        prev = None
        current = head

        while current is not None:
            if current.val == val:

                if prev is None:
                    current = current.next
                    head = current
                    continue
                else:
                    prev.next = current.next
                    current = current.next

            else:
                prev = current
                current = current.next

        return head

