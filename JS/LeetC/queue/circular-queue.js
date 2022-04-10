// Implement a queue using "circular" array

class MyCircularQueue {
  constructor(k = 5) {
    this.size = k;
    this.data = [];
    this.head = null;
    this.tail = null;
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
      this.head = 0;
      this.tail = 0;
    } else {
      this.tail = (this.tail + 1) % this.size;
    }

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
      this.tail = null;
      this.head = null;
      return true;
    }

    this.head = (this.head + 1) % this.size;
    return true;
  }

  // isEmpty : void -> bool
  isEmpty() {
    return this.head === null || this.tail === null;
  }

  isFull() {
    return (
      this.head !== null &&
      this.tail !== null &&
      ((this.head === 0 && this.tail === this.size - 1) ||
        (this.head > this.tail && this.head - this.tail === 1))
    );
  }
}

module.exports = MyCircularQueue;
