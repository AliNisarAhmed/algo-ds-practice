class Solution:
    def hasCycle(self, head):

        if head is None:
            return False

        current = head
        runner = head.next

        while runner is not None and runner.next is not None:
            if runner is current:
                return True
            runner = runner.next.next
            current = current.next

        return False
