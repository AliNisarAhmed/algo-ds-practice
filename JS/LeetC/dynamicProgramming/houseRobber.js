function rob(arr, memo = {}, start = 0, end = arr.length - 1) {
	if (memo[start]) {
		return memo[start];
	}

	if (end === start) {
		memo[start] = arr[start];
		return arr[start];
	}

	if (end - start === 1) {
		memo[start] = Math.max(arr[start], arr[end]);
		return memo[start];
	}

	let midpoint = Math.floor(start + (end - start) / 2);

	let results = [];

	for (let i = start; i <= midpoint; i++) {
		if (i + 2 <= end) {
			let r = rob(arr, memo, i + 2, end);
			memo[start] = arr[i] + r;
			results.push(memo[start]);
		} else {
			memo[start] = arr[i];
			results.push(memo[start]);
		}
	}

	return Math.max(...results);
}

console.log(rob([2, 7, 9, 3, 1]));

// function helper(arr, memo) {
// 	if (arr.length === 1) {
// 		return arr[0];
// 	}

// 	if (arr.length === 2) {
// 		return Math.max(arr[0], arr[1]);
// 	}
// }
