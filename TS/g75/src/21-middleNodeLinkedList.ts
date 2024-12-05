import type { ListNode } from "./00-ListNode";

function middleNode(head: ListNode | null): ListNode | null {
  if (!head) {
    return null;
  }
  let slow: ListNode | null = head;
  let fast: ListNode | null = head;

  while (fast && fast.next) {
    slow = slow ? slow.next : null;
    fast = fast.next.next;
  }

  return slow;
}
