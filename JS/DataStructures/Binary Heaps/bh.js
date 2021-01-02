// Max Binary Heap

class BinaryHeap {
	constructor() {
		this.data = [];
	}

	leftChildIndex(index) {
		return index * 2 + 1;
	}

	rightChildIndex(index) {
		return index * 2 + 2;
	}

	parentIndex(index) {
		return Math.floor((index - 1) / 2);
	}

	insert(v) {
		this.data.push(v);
		let newNodeIndex = this.data.length - 1;
		let newNode = this.data[newNodeIndex];
		let parentIndex = this.parentIndex(newNodeIndex);
		let parent = this.data[parentIndex];
		while (parent && newNodeIndex > 0 && newNode > parent) {
			// swap the parent with the current node
			[this.data[parentIndex], this.data[newNodeIndex]] = [
				this.data[newNodeIndex],
				this.data[parentIndex],
			];
			newNodeIndex = parentIndex;
			parentIndex = this.parentIndex(newNodeIndex);
			parent = this.data[parentIndex];
		}
		return this;
	}

	// also called extractMax or extractMin for Max or Min Binary Heap
	delete() {
		let max = this.data[0];
		this.data[0] = this.data.pop();
		let trickleNodeIndex = 0;

		while (this.hasGreaterChild(trickleNodeIndex)) {
			let largerChildIndex = this.calculateLargerChildIndex(trickleNodeIndex);

			[this.data[largerChildIndex], this.data[trickleNodeIndex]] = [
				this.data[trickleNodeIndex],
				this.data[largerChildIndex],
			];
			trickleNodeIndex = largerChildIndex;
		}

		return max;
	}

	hasGreaterChild(index) {
		let elem = this.data[index],
			leftChild = this.data[this.leftChildIndex(index)],
			rightChild = this.data[this.rightChildIndex(index)];

		return (leftChild && leftChild > elem) || (rightChild && rightChild > elem);
	}

	calculateLargerChildIndex(index) {
		let leftChildIndex = this.leftChildIndex(index),
			rightChildIndex = this.rightChildIndex(index),
			leftChild = this.data[leftChildIndex],
			rightChild = this.data[rightChildIndex];

		if (!rightChild) {
			return leftChildIndex;
		}

		if (!leftChild) {
			return rightChildIndex;
		}

		return rightChild > leftChild ? rightChildIndex : leftChildIndex;
	}
}

let bh = new BinaryHeap();

bh.insert(80).insert(88).insert(87).insert(16).insert(100).insert(50).insert(2);
// .insert(15)
// .insert(25)
// .insert(8)
// .insert(12)
// .insert(3);

console.log(bh.data);

bh.delete();

console.log(bh);
