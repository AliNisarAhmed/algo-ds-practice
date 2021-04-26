class Solution {
	constructor(nums) {
		this.nums = nums;
		this._internal = [...nums];
	}

	reset() {
		this.nums = [...this._internal]
		return this.nums;
	}

	shuffle() {
		for (let i = this.nums.length - 1; i >= 0; i--) {
			let rand = this.randBetween(0, i);
			[ this.nums[rand], this.nums[i]] = [this.nums[i], this.nums[rand]];
		}

		return this.nums;
	}

	// end included
	randBetween(start, end) {
		return Math.floor(Math.random() * (end - start + 1) + start);
	}
}