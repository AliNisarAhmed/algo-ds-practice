class DoublyListNode {
  constructor(val, next = null, prev = null) {
    this.val = val;
    this.next = next;
    this.prev = prev;
  }
} 

class DoublyLinkedList {
  constructor(head = null, tail = null) {
    this.head = head;
    this.tail = tail;
  }

  insertAtEnd(val) {
    let newNode = new DoublyListNode(val);

    if (!this.head) {
      this.head = newNode;
      this.tail = newNode;
      return this;
    } 

    this.tail.next = newNode;
    newNode.prev = this.tail;
    this.tail = newNode;
  }

  removeFromFront() {
    if (!this.head) {
      return null;
    }

    let removed = this.head;

    this.head = this.head.next;
    this.head.prev = null;
    return removed;
  }
}
