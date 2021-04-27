class MinHeap {
	constructor() {
		this.list = [];
	}

	leftChildIndex(n) {
		return 2 * n + 1;
	}

	rightChildIndex(n) {
		return 2 * n + 2;
	}

	parentIndex(n) {
		return Math.floor((n - 1) / 2);
	}

	extractMin() {
		// swapping the first and last
		[this.list[0], this.list[this.list.length - 1]] = [
			this.list[this.list.length - 1],
			this.list[0],
		];

		// remove the first element which is now at the last index
		let removed = this.list[this.list.length - 1];

		this.bubbleDown();

		return removed;
	}

	bubbleDown() {
		let currentIndex = 0;
		let current = this.list[currentIndex];
		let length = this.list.length;
		let leftChildIndex = this.leftChildIndex(currentIndex);
		let left = this.list[leftChildIndex];
		let rightChildIndex = this.rightChildIndex(currentIndex);
		let right = this.list[rightChildIndex];

		while ((left && left > current) || (right && right > current)) {

			if (left > right) {
				[this.list[currentIndex], this.list[leftChildIndex]]
					= [this.list[leftChildIndex], this.list[currentIndex]];
				current = leftChildIndex;

			} else {
				[this.list[currentIndex], this.list[rightChildIndex]]
					= [this.list[rightChildIndex], this.list[currentIndex]];
				current = rightChildIndex;
			}

			leftChildIndex = this.leftChildIndex(current);
			left = this.list[leftChildIndex];
			rightChildIndex = this.rightChildIndex(current);
			right = this.list[rightChildIndex];

		}
	}

	insert(n) {
		this.list.push(n);
		this.bubbleUp(this.list.length - 1);
		return this;
	}

	bubbleUp(newNodeIndex) {
		let parentIndex = this.parentIndex(newNodeIndex);

		while (parentIndex >= 0) {
			if (this.list[parentIndex] > this.list[newNodeIndex]) {
				// swap the elements at two indices
				[this.list[parentIndex], this.list[newNodeIndex]] = [
					this.list[newNodeIndex],
					this.list[parentIndex],
				];
			}
			newNodeIndex = parentIndex;
			parentIndex = this.parentIndex(newNodeIndex);
		}
	}
}

let bh = new MinHeap();

bh.insert(80).insert(88).insert(87).insert(16).insert(100).insert(50).insert(2);

console.log(bh);
