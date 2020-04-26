class Node {
  constructor(v) {
    this.value = v;
    this.next = null;
    this.prev = null;
  }
}

class DoublyLinkedList {
  constructor() {
    this.length = 0;
    this.head = null;
    this.teail = null;
  }

  push(v) {
    let node = new Node(v);
    if (!this.head) {
      this.head = this.tail = node;
    } else {
      this.tail.next = node;
      node.prev = this.tail;
      this.tail = node;
    }
    this.length++;
    return this;
  }

  pop() {
    let removed = this.tail;
    if (this.length === 0)
      return null;
    if (this.length === 1) {
      this.head = this.tail = null;
    } else {
      this.tail.prev.next = null;
      this.tail = removed.prev;
      // sever the connection of the removed element to the list
      removed.prev = null;
    }

    this.length--;
    return removed;
  }

  shift() {
    let removed = this.head;
    if (this.length === 0)
      return null;
    if (this.length === 1) {
      this.head = this.tail = null;
    } else {
      removed.next.prev = null;
      this.head = removed.next;
      removed.next = null;
    }

    this.length--;
    return removed;
  }

  unshift(v) {
    let newNode = new Node(v);
    if (!this.head) {
      this.head = this.tail = newNode;
    } else {
      newNode.next = this.head;
      this.head.prev = newNode;
      this.head = newNode;
    }

    this.length++;
    return this;
  }

  get(index) {
    let len = this.length;
    if (index < 0 || index >= len) {
      return null;
    }

    let midpoint = Math.floor(len / 2);
    if (index <= midpoint) {
      let current = this.head;
      while (index > 0) {
        current = current.next;
        index--;
      }
      return current;
    } else {
      let current = this.tail;
      while (len - 1 != index) {
        current = current.prev;
        len--;
      }
      return current;
    }
  }

}

var list = new DoublyLinkedList();
list.push(1).push(2).push(3).push(4).push(5);

module.exports = DoublyLinkedList;