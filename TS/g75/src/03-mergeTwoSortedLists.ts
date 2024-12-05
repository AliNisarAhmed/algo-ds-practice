class ListNode {
  val: number;
  next: ListNode | null;
  constructor(val?: number, next?: ListNode | null) {
    this.val = val === undefined ? 0 : val;
    this.next = next === undefined ? null : next;
  }
}

function mergeTwoLists(
  list1: ListNode | null,
  list2: ListNode | null,
): ListNode | null {
  let sentinel: ListNode | null = new ListNode(-1, null);
  let current: ListNode | null = sentinel;

  while (list1 && list2) {
    if (list1.val > list2.val) {
      current!.next = list2;
      list2 = list2.next;
    } else {
      current!.next = list1;
      list1 = list1.next;
    }
    current = current ? current.next : null;
  }

  if (!list1 && list2) {
    current!.next = list2;
  }

  if (!list2 && list1) {
    current!.next = list1;
  }

  return sentinel.next;
}
