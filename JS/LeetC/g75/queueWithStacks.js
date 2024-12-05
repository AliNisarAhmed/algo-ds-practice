class MyQueue {

  constructor() {
    this.back = [];
    this.front = [];
  }

  push(x) {
    this.back.push(x)
  }

  pop() {
    if (this.empty()) {
      return null;
    }

    if (this.front.length > 0) {
      return this.front.pop();
    }

    this.#moveBackToFront();

    return this.front.pop();
  }

  peek() {
    if (this.empty()) {
      return null;
    }

    if (this.front.length > 0) {
      return this.front[this.front.length - 1]
    }

    this.#moveBackToFront();

    return this.front[this.front.length - 1];
  }

  empty() {
    return this.back.length === 0 && this.front.length === 0;
  }

  #moveBackToFront() {
    while (this.back.length > 0) {
      this.front.push(this.back.pop());
    }
  }
}

main();

function main() {
  let q = new MyQueue();
  q.push(1)
  q.push(2)
  console.log(q.peek())
  console.log(q.pop())
  console.log(q.empty())
}
