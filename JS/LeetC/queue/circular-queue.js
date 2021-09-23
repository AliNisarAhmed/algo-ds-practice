// Implement a queue using "circular" array

class MyCircularQueue {
  constructor(k) {
    this.size = k;
    this.data = [];
    this.head = 0;
    this.tail = 0;
  }

  // Gets the front item from the queue. If the queue is empty, return -1
  Front() {
    if (!this.isEmpty()) {
      return this.data[this.head];
    }

    return -1;
  }

  // Gets the last item from the queue. If the queue is empty, return -1
  Rear() {
    if (!this.isEmpty()) {
      return this.data[this.tail];
    }

    return -1;
  }

  // enQueue :: int -> bool
  enQueue(val) {
    if (this.isFull()) {
      return false;
    }

    if (this.isEmpty()) {
      this.data[this.head] = val;
      return true;
    }

    this.tail = (this.tail + 1) % this.size;
    this.data[this.tail] = val;
    return true;
  }

  // deQueue :: void -> bool
  deQueue() {
    if (this.isEmpty()) {
      return false;
    }

    if (this.tail === this.head) {
      this.data[this.tail] = undefined;
      return true;
    }

    this.head = (this.head + 1) % this.size;
    return true;
  }

  // isEmpty : void -> bool
  isEmpty() {
    return this.tail === this.head && this.data[this.tail] === undefined;
  }

  isFull() {
    return (
      (this.head === 0 && this.head !== this.tail && this.tail === this.size - 1) || this.head - this.tail === 1
    );
  }
}
