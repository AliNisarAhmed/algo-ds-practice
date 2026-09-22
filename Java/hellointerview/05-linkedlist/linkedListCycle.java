public class Solution {
  public Boolean hasCycle(ListNode head) {
    ListNode slow = null;
    ListNode fast = head;

    while (fast != null && fast.next != null) {
      fast = fast.next.next;
      slow = slow.next;

      if (fast.equals(slow)) {
        return true;
      }
    }
    return false;
  }

}
