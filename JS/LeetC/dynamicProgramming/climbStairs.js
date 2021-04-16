function climbStairs(n, memo = {}) {
	if (n <= 0) {
		return 0;
	}

	if (n === 1) {
		return 1;
	}

	if (n === 2) {
		return 2;
	}

	let prev;
	if (!memo[n - 1]) {
		prev = memo[n - 1] = climbStairs(n - 1, memo);
	} else {
		prev = memo[n - 1]
	}

	let prev2;

	if (!memo[n - 2]) {
		prev2 = memo[n - 2] = climbStairs(n - 2, memo);
	} else {
		prev2 = memo[n - 2];
	}

	return prev + prev2
}

function climbStairs(n) {
	if (n === 1) {
		return 1;
	}

	let dp = [1, 2];

	for (let i = 2; i < n; i++) {
		dp[i] = dp[i - 1] + dp[i - 2];
	}

	return dp[n - 1];
}