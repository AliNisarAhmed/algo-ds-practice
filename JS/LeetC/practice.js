function removeDups(head) {
  if (!head) return head;

  let set = new Set();

  let current = head; 
  let prev = head;

  while (current) {
    if (set.has(current.val)) {
      current = current.next
    } else { 
      set.add(current.val); 
      prev.next = current;
      prev = prev.next; 
      current = current.next;
    }
  }

  return head;
}
