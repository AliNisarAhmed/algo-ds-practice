class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function reverseList(head: ListNode | null): ListNode | null {
  if (!head || !head.next) {
    return head;
  }

  const rest = reverseList(head.next);
  head.next.next = head;
  head.next = null;
  return rest
}

function reverseListIter(head: ListNode | null): ListNode | null {
  let prev = null;
  let current = head;

  while (current) {
    let temp = current.next;
    current.next = prev;
    prev = current;
    current = temp;
  }

  return current;
}
