function mergeKLists(lists) {
  let dummyHead = { val: -1, next: null };
  let prev = dummyHead;

  let minNode = null;
  let minNodeIndex = 0;

  while (lists.some(n => n !== null)) {

    for (let i = 0; i < lists.length; i++) {
      if (!minNode) {
        minNode = lists[i];
        minNodeIndex = i;
        continue;
      } 
      if (lists[i] && lists[i].val < minNode.val) {
        minNode = lists[i];
        minNodeIndex = i;
      }
    }

    prev.next = minNode;
    minNode = null;
    lists[minNodeIndex] = lists[minNodeIndex].next;
  
    prev = prev.next;
  }

  return dummyHead.next;

}
