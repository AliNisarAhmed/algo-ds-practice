class MaxHeap {
  constructor() {
    this.data = [];
  }

  getRoot() {
    return this.data[0];
  }

  getLastNode() {
    return this.data[this.data.length - 1];
  }

  leftChildIndex(idx) {
    return idx * 2 + 1;
  }

  rightChildIndex(idx) {
    return idx * 2 + 2;
  }

  parentIndex(idx) {
    return idx - 1 / 2;
  }

  insert(val) {
    this.data.push(val);
    let newNodeIndex = this.data.length - 1;
    while (
      newNodeIndex > 0 &&
      this.data[newNodeIndex] > this.data[parentIndex]
    ) {
      let parentIndex = this.parentIndex(newNodeIndex);

      [this.data[newNodeIndex], this.data[parentIndex]] = [
        this.data[parentIndex],
        this.data[newNodeIndex],
      ];

      newNodeIndex = parentIndex;
    }

    return this;
  }

  extractMax() {
    this.data[0] = this.data.pop();

    let trickleNodeIndex = 0;

    while (hasGreaterChild(trickleNodeIndex)) {
      let largerChildIndex = calculateLargerChildIndex(trickleNodeIndex);

      [this.data[trickleNodeIndex], this.data[largerChildIndex]] = [
        this.data[largerChildIndex],
        this.data[trickleNodeIndex],
      ];

      trickleNodeIndex = largerChildIndex;
    }
  }

  hasGreaterChild(index) {
    return (
      (this.data[this.leftChildIndex(index)] &&
        this.data[this.leftChildIndex(index)] > this.data[index]) ||
      (this.data[this.rightChildIndex(index)] &&
        this.data[this.rightChildIndex(index)])
    );
  }

  calculateLargerChildIndex(index) {
    if (!this.data[this.rightChildIndex(index)]) {
      return this.leftChildIndex(index);
    }

    if (this.data[this.rightChildIndex(index)] > this.data[this.leftChildIndex(index)]) {
      return this.rightChildIndex(index);
    } else {
      return this.leftChildIndex(index);
    }
  }
}
