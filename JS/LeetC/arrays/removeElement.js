function removeElement(nums, val) {


	let j = 0;
	// j keeps track of the first val
	while (nums[j] !== val && j < nums.length) {
		j++;
	}

	let i = j - 1;

	while (j < nums.length) {
		// find the next non-val

		while (nums[j] === val) {
			j++;
		}

		nums[i + 1] = nums[j];

		i++;
	}

	return i;
}

console.log(removeElement([3, 2, 2, 3], 3))