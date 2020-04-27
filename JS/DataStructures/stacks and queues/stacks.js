class Node {
  constructor(v) {
    this.value = v;
    this.next = null;
  }
}

// we cant use a linked list directly because
// for stacks, push and pop is O(1), whereas for
// linked list pop() is O(n)

class Stack {
  constructor() {
    this.first = null;
    this.last = null;
    this.size = 0;
  }

  push(v) {
    let newNode = new Node(v);
    if (!this.first) {
      this.first = this.last = newNode;
    } else {
      newNode.next = this.first;
      this.first = newNode;
    }
    return ++this.size;
  }

  pop() {
    if (!this.first)
      return null;
    let removed = this.first;
    if (this.size === 1) {
      this.first = this.last = null;
    } else {
      this.first = this.first.next;
    }
    this.size--;
    return removed.value;
  }

}