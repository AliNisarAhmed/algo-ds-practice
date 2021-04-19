function rob(arr) {
	const memo = {};
	return helper(arr, memo, 0);
}

function helper(arr, memo, current) {
	if (memo[current]) {
		return memo[current];
	}

	if (current >= arr.length) {
		return 0;
	}

	if (current === arr.length - 1) {
		memo[current] = arr[current];
		return arr[current];
	}

	memo[current] = Math.max(
		helper(arr, memo, current + 1),
		helper(arr, memo, current + 2) + arr[current]
	);

	return memo[current];
}

console.log(rob([1, 2]));

function rob(arr) {
	if (arr.length === 0) {
		return 0;
	}

	let maxRobbedAmount = [];
	let n = arr.length;

	maxRobbedAmount[n] = 0;
	maxRobbedAmount[n - 1] = arr[n - 1];

	for (let i = n - 2; i >= 0; i--) {
		maxRobbedAmount[i] = Math.max(maxRobbedAmount[i + 1], maxRobbedAmount[i + 2] + arr[i]);
	}

	return maxRobbedAmount[0];
}

function rob(arr) {
	if (arr.length === 0) {
		return 0;
	}

	let n = arr.length;
	let robNext = arr[n - 1];
	let robNextPlusOne = 0;

	for (let i = n - 2; i >= 0; i--) {
		current = Math.max(robNext, robNextPlusOne + arr[i]);

		robNextPlusOne = robNext;
		robNext = current;
	}

	return robNext;
}