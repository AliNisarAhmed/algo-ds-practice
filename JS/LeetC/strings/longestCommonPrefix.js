function longestCommonPrefix(arr) {
	if (arr.length === 0) return ''
	if (arr.length === 1) return arr[0];
	let minString = Math.min(...arr.map(s => s.length));
	let i = 0;
	while (i < minString) {
		if (!checkMatchesAtIndex(i, arr)) {
			return arr[0].slice(0, i);
		}
		i++;
	}

	return arr[0].slice(0, i);
}

function checkMatchesAtIndex(i, arr) {
	for (let j = 0; j < arr.length - 1; j++) {
		if (arr[j][i] !== arr[j + 1][i]) {
			return false;
		}
	}

	return true;
}

// console.log(longestCommonPrefix(["flower","flow","flight"]));
console.log(longestCommonPrefix(["ab", "a"]));