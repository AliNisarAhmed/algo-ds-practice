class DoublyListNode {
  constructor(val, next = null, prev = null) {
    this.val = val;
    this.next = next; 
    this.prev = prev;
  }
}

class MyDoublyLinkedList {
  
  constructor(node = null) {
    this.head = node;   
  }

  getNodeAtIndex(index) {
    if (index < 0) return null;

    if (!head) return null;

    let current = this.head;

    while (current) {
      if (index < 0) return null;
      
      if (index === 0) {
        return current;
      }

      index--;
      current = current.next;
    }

    return null;
  }

  get(index) {
    let node = this.getNodeAtIndex(index);
   return node === null ? -1 : node;
  }

  addAtHead(val) {
    let newNode = new DoublyListNode(val);

    if (!this.head) return newNode;

    newNode.next = this.head;
    this.head.prev = newNode.next;

    this.head = newNode; 

    return newNode;
  }
}
