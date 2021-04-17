function removeDuplicates(nums) {
	let i = 0;
	let j = 0;

	while (j < nums.length) {

		if (nums[i] !== nums[j]) {
			nums[i] = nums[j];
		}

		while(nums[j] === nums[i]) {
			j++;
		}

		i++;
	}

	nums.length = i;

	return nums.length;
}

console.log(removeDuplicates([1,2]));