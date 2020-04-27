class Node {
  constructor(v) {
    this.value = v;
    this.next = null;
  }
}

class Queue {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  enqueue(v) {
    let newNode = new Node(v);
    if (!this.first) {
      this.first = this.last = newNode;
    } else {
      this.last.next = newNode;
    }
    this.size++;
    return this;
  }

  dequeue() {
    if (!this.first)
      return null;
    let removed = this.first;
    if (this.size === 1) {
      this.first = this.last = null;
    } else {
      this.first = this.first.next;
    }
    this.size--;
    return removed;
  }
}