function maxSubArray(nums) {
	let maxSubArray = Number.NEGATIVE_INFINITY;

	for (let i = 0; i < nums.length; i++) {
		currentSubArray = 0;

		for (let j = i; j < nums.length; j++) {
			currentSubArray += nums[j];
			maxSubArray = Math.max(maxSubArray, currentSubArray);
		}
	}

	return maxSubArray;
}

function maxSubArray(nums) {
	let currentSubArray = nums[0];
	let maxSubArray = nums[0];

	for (let i = 1; i < nums.length; i++) {
		currentSubArray = Math.max(nums[i], currentSubArray + nums[i]);
		maxSubArray = Math.max(currentSubArray, maxSubArray);
	}

	return maxSubArray;
}
