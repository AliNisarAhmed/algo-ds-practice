class MaxBinaryHeap {
	constructor() {
    this.values = [];
	}

	insert(v) {
		this.values.push(v);
		let index = this.values.length - 1;
		let parentIndex = Math.floor((index - 1) / 2);
		let parent = this.values[parentIndex];
		while (parent < v && parentIndex >= 0) {
			this.values[parentIndex] = v;
			this.values[index] = parent;
			index = parentIndex;
			parentIndex = Math.floor((parentIndex - 1) / 2);
			parent = this.values[parentIndex];
		}
		return this;
	}

	// Also called remove
	// return the largest value in the heap (which will be the root)
	// extracting the largest value unbalances the heap, so we need to
	// rearrange elements into a valid binary heap.
	extractMax() {
		const { values } = this;

    // swap the first and the last
    this.swap(0, this.values.length - 1);

    // now the last is the one that we wanted to remove
    const removed = values.pop();

    // start the "sinking down" of the now root
		let parentIndex = 0;
		while (parentIndex < values.length) {
			const v = values[parentIndex];
			const leftChildIdx = 2 * parentIndex + 1;
			const rightChildIdx = 2 * parentIndex + 2;
			const left = values[leftChildIdx];
      const right = values[rightChildIdx];

      if (!left) {
        if (right && right > v) {
          this.swap(rightChildIdx, parentIndex);
          parentIndex = rightChildIdx;
        }
        break;
      } else if (!right) {
        if (left && left > v) {
          this.swap(leftChildIdx, parentIndex);
          parentIndex = leftChildIdx;
        }
        break;
      } else if (left > v || right > v) {
				if (left >= right) {
          this.swap(leftChildIdx, parentIndex);
          parentIndex = leftChildIdx;
				} else {
          this.swap(rightChildIdx, parentIndex);
          parentIndex = rightChildIdx;
        }
      }
      break;
    }

    return removed;
  }

  // extractMax - recursive
  remove() {
    const { values } = this;
    let swap = this.swap.bind(this);
    swap(0, values.length - 1);
    const removed = values.pop();

    const sinkDown = (parentIndex) => {
      let v = values[0];
      let leftChildIdx = parentIndex * 2 + 1;
      let rightChildIdx = parentIndex * 2 + 2;
      let left = values[leftChildIdx];
      let right = values[rightChildIdx];

      if (!left) {
        if (right && right > v) {
          swap(rightChildIdx, parentIndex);
          sinkDown(rightChildIdx);
        }
      } else if (!right) {
        if (left && left > v) {
          swap(leftChildIdx, parentIndex);
          sinkDown(leftChildIdx)
        }
      } else if (left > v || right > v) {
				if (left >= right) {
          swap(leftChildIdx, parentIndex);
          sinkDown(leftChildIdx);
				} else {
          swap(rightChildIdx, parentIndex);
          sinkDown(rightChildIdx);
        }
      }

      return removed;
    };

    return sinkDown(0);
  }

  swap(first, second) {
    [ this.values[first], this.values[second] ] =
      [ this.values[second], this.values[first] ];
  }
}

const heap = new MaxBinaryHeap();
heap.insert(100).insert(200).insert(150).insert(300).insert(400).insert(500);
const max = heap.remove();
console.log('max', max);
console.log('heap', heap)
