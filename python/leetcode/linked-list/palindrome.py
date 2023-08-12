class Solution:
    def isPalindrome(self, head):
        if head is None:
            return True

        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        result = True
        first_position = head
        second_position = second_half_start

        while result and second_position is not None:
            if first_position.val != second_position.val:
                result = False

            first_position = first_position.next
            second_position = second_position.next

        first_half_end.next = self.reverse_list(second_half_start)
        return result

    def end_of_first_half(self, head):
        fast = head
        slow = head

        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverse_list(self, head):
        prev = None
        current = head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    # ---------------------------------------------------------

    def isPalindrome_recur(self, head):
        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next

            return True

        return recursively_check()
