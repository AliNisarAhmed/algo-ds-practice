class Solution:

    def getIntersectionNode(self, headA, headB):
        len_a = self.len(headA)
        len_b = self.len(headB)

        longer = headA
        shorter = headB

        if len_a != len_b:
            diff = abs(len_a - len_b)

            shorter = headA if len_a < len_b else headB
            longer = headA if len_a > len_b else headB

            while diff > 0:
                longer = longer.next
                diff -= 1

        while longer is not None and shorter is not None:
            if longer == shorter:
                return shorter

            longer = longer.next
            shorter = shorter.next

        return None

    def len(self, head):
        len = 0
        current = head
        while current is not None:
            current = current.next
            len += 1

        return len
