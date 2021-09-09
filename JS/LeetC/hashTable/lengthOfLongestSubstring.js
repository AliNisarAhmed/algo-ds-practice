function lengthOfLongestSubstring(str) {
	if (str.length === 1) return 1;
	let obj = {};

	let left = 0;
	let right = 0;
	let max = 0;

	while (right < str.length) {
		let current = str[right];
		let index = obj[current];

		if (index !== undefined && index >= left && index < right) {
			// if we have already seen it, and its index is within current window
			left = index + 1;
		}

		max = Math.max(max, right - left + 1);

		obj[current] = right;
		right++;
	}
	return max;
}

console.log(lengthOfLongestSubstring('abcabcbb'));
