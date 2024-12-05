/* ListNode = { val: val, next: ListNode | null }
  *
  */

function hasCycle(head) {
  if (head === null) {
    return false;
  }

  let slow = head;
  let fast = head.next;

  while (fast && fast.next && fast.next.next) {
    if (fast === slow) {
      return true;
    }

    slow = slow.next;
    fast = fast.next.next;
  }

  return false;
}
