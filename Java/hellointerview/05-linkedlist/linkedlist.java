public class LinkedList {

  public int length(ListNode head) {
    var current = head;
    var length = 0;
    if (head == null) {
      return length;
    }
    while (current != null) {
      length++;
      current = current.next;
    }
    return length;
  }

  public ListNode midpoint(ListNode head) {
    var fast = head;
    var slow = head;

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
      var next = current.next;
      current.next = prev;
      prev = current;
      current = next;
    }
  }
}
