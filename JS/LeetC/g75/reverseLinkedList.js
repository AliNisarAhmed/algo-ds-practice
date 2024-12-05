function reverseList(head) {
  if (!head || !head.next) {
    return head;
  }

  let current = head;
  let prev = null;

  while (current) {
    let temp = current.next;
    current.next = prev;
    prev = current;
    current = temp
  }

  return prev;
}
