function removeElement(nums, val) {
	if (nums.length === 0) {
		return 0;
	}

	let j = 0;
	// j keeps track of the first val
	while (nums[j] !== val && j < nums.length) {
		j++;
	}

	if (j >= nums.length) {
		return nums.length;
	}

	let i = j - 1;

	if (j === 0) {
		i = 0;
		while (nums[i] === val && i < nums.length) {
			i++;
		}

		if (i >= nums.length) {
			nums.length = 0;
			return 0;
		} else {
			[nums[i], nums[j]] = [nums[j], nums[i]];
			[i, j] = [j, i];
		}
	}

	while (j < nums.length) {
		// find the next non-val

		while (nums[j] === val && j < nums.length) {
			j++;
		}

		if (j < nums.length) {
			[nums[i + 1], nums[j]] = [nums[j], nums[i + 1]];

			i++;
			j++;
		}
	}

	nums.length = i + 1;

	return i + 1;
}

function removeElement(nums, val) {
	let i = 0;

	for (let j = 0; j < nums.length; j++) {
		if (nums[j] !== val) {
			nums[i] = nums[j];
			i++;
		}
	}

	return i;
}

function removeElement(nums, val) {
	let i = 0;
	let n = nums.length;
	while (i < n) {
		if (nums[i] === val) {
			nums[i] = nums[n - 1];
			n--;
		} else {
			i++;
		}
	}

	return n;
}

console.log(removeElement([4, 1, 2, 3, 5], 4));
