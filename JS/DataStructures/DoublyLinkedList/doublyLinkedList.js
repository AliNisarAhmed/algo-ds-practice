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
    this.tail = null;
  }

  see() {
		// to "see" the current list
		let current = this.head;
		let res = '';
		while (current) {
			res += `${current.value} -> `;
			current = current.next;
		}
		console.log(res);
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

  set(index, value) {
    const foundNode = this.get(index);
    if (foundNode) {
      foundNode.value = value;
      return true;
    }
    return false;
  }

  insert(index, value) {
    if (index < 0 || index > this.length)
      return false;
    if (index === 0) {
      this.unshift(value);
    } else if (index === this.length) {
      this.push(value);
    } else {
      let newNode = new Node(value);
      const current = this.get(index);
      let prev = current.prev;
      prev.next = newNode;
      newNode.prev = prev;
      newNode.next = current;
      current.prev = newNode;
      this.length++;
    }
    return true;
  }

  remove(index) {
    if (index < 0 || index >= this.length)
      return null;
    if (index === 0)
      return this.shift();
    if (index === this.length - 1)
      return this.pop();
    let current = this.get(index);
    current.prev.next = current.next;
    current.next.prev = current.prev;
    current.prev = current.next = null;
    this.length--;
    return current;
  }

  reverse() {
    if(this.length <= 1) return this;
    [this.head, this.tail] = [this.tail, this.head];
    let next;
    let prev = null;
    let current = this.tail;
    while(current) {
      next = current.next;
      current.next = prev;
      current.prev = next;
      prev = current;
      current = next;
    }
    return this;
  }

}

var list = new DoublyLinkedList();
list.push(1).push(2).push(3).push(4).push(5);

module.exports = DoublyLinkedList;