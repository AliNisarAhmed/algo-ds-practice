
# Floyds Tortoise and Hare algo

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        tortoise = head
        hare = head

        while hare is not None and hare.next is not None:
            tortoise = tortoise.next
            hare = hare.next.next
            if hare is tortoise:
                break

        if hare is None or hare.next is None:
            return None

        hare = head
        while hare is not tortoise:
            hare = hare.next
            tortoise = tortoise.next

        return hare
