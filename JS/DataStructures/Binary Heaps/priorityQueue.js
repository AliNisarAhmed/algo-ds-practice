class Node {
	constructor(v, p) {
		this.value = v;
		this.priority = p;
	}
}

class PriorityQueue {
	constructor() {
		this.values = [];
	}

	enqueue(v, p) {
		let node = new Node(v, p);
		this.values.push(node);
		let index = this.values.length - 1;
		let parentIndex = Math.floor((index - 1) / 2);
		let parent = this.values[parentIndex];

		while (parentIndex >= 0 && node.priority < parent.priority) {
			this.swap(parentIndex, index);
			index = parentIndex;
			parentIndex = Math.floor((index - 1) / 2);
			parent = this.values[parentIndex];
		}
		return this;
	}

	displayValues() {
		return this.values.map(v => v.priority);
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
				if (right && v.priority > right.priority) {
					this.swap(rightChildIdx, parentIndex);
					parentIndex = rightChildIdx;
				}
				break;
			} else if (!right) {
				if (left && v.priority > left.priority) {
					this.swap(leftChildIdx, parentIndex);
					parentIndex = leftChildIdx;
				}
				break;
			} else if (v.priority > left.priority || v.priority > right.priority) {
				if (left.priority < right.priority) {
					this.swap(leftChildIdx, parentIndex);
					parentIndex = leftChildIdx;
				} else {
					this.swap(rightChildIdx, parentIndex);
					parentIndex = rightChildIdx;
				}
			} else {
				break;
			}
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
				if (right && v.priority > right.priority) {
					swap(rightChildIdx, parentIndex);
					sinkDown(rightChildIdx);
				}
			} else if (!right) {
				if (left && v.priority > left.priority) {
					swap(leftChildIdx, parentIndex);
					sinkDown(leftChildIdx);
				}
			} else if (v.priority > left.priority || v.priority > right.priority) {
				if (left.priority < right.priority) {
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
		[this.values[first], this.values[second]] = [
			this.values[second],
			this.values[first],
		];
	}
}

let pq = new PriorityQueue();

pq.enqueue(100, 1)
	.enqueue(200, 2)
	.enqueue(300, 3)
	.enqueue(400, 4)
  .enqueue(500, 1)
	.enqueue(600, 3)
	.enqueue(200, 2)
	.enqueue(300, 3)


let removed = pq.extractMax();

while(removed) {
	console.log(removed);
	removed = pq.extractMax();
}

console.log(pq.values);

module.exports = PriorityQueue;