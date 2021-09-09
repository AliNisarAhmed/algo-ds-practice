// Using a hashmap - O(1) add and O(n) find

class TwoSum {
	constructor() {
		this.numbers = {};
	}

	add(n) {
		this.numbers[n] = this.numbers[n] ? this.numbers[n] + 1 : 1;
		return this;
	}

	find(k) {
		for (let [key, v] of Object.entries(this.numbers)) {
			let comple = k - key;
			if (key !== comple) {
				if (this.numbers[comple] !== undefined) {
					return true;
				}
			} else if (v > 1) {
				return true;
			}
		}

		return false;
	}
}

// sorted list - O(1) add (if not sorted on each addition) and O(nlogn) find (sort before each find)

// class TwoSum {
// 	constructor() {
// 		this.numbers = [];
// 	}

// 	add(n) {
// 		if (this.numbers.length === 0) {
// 			this.numbers = [n];
// 		} else {
// 			for (let i = 0; i < this.numbers.length; i++) {
// 				if (this.numbers[i] > n) {
// 					this.numbers.splice(i, 0, n);
// 					return this;
// 				}
// 			}
// 			this.numbers.push(n);
// 		}
// 		return this;
// 	}

// 	find(k) {
// 		let left = 0;
// 		let right = this.numbers.length - 0;

// 		while (left < right) {
// 			let n1 = this.numbers[left];
// 			let n2 = this.numbers[right];
// 			if (n1 + n2 === k) {
// 				return true;
// 			}

// 			if (n1 + n2 < k) {
// 				left++;
// 			} else {
// 				right--;
// 			}
// 		}

// 		return false;
// 	}
// }

console.log(new TwoSum().add(1).add(3).add(5).find(4));
