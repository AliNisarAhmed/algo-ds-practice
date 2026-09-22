public class Solution {
  public boolean isPalindrome(ListNode head) {
    ListNode midpoint = findMidpoint(head);
    ListNode newHead = reverse(midpoint);

    ListNode first = head;
    ListNode second = newHead;

    while (second != null) {
      if (first.val != second.val) {
        return false;
      }
      first = first.next;
      second = second.next;
    }
    return true;
  }

  public ListNode findMidpoint(ListNode head) {
    ListNode slow = head;
    ListNode fast = head;

    while (fast != null && fast.next != null) {
      fast = fast.next.next;
      slow = slow.next;
    }

    return slow;
  }

  public ListNode reverse(ListNode head) {
    ListNode prev = null;
    ListNode current = head;
    while (current != null) {
      ListNode next = current.next;
      current.next = prev;
      prev = current;
      current = next;
    }
    return prev;
  }
}
