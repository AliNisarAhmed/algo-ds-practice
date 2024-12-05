/*
 * Node.val Node.next
 */

function mergeTwoLists(list1, list2) {
  if (!list1 && !list2) {
    return null;
  }

  if (!list1) {
    return list2;
  }

  if (!list2) {
    return list1;
  }

  let current = {};
  let head = current;

  while (list1 && list2) {
    if (list1.val <= list2.val) {
      current.next = list1;
      list1 = list1.next;
    } else if (list2.val < list1.val) {
      current.next = list2;
      list2 = list2.next;
    }
    current = current.next;
  }

  if (!list1) {
    current.next = list2;
  }

  if (!list2) {
    current.next = list1;
  }

  return head.next;
}
