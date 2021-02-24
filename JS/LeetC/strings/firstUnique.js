function firstUniqChar(str) {
	let obj = {};

	for (let c of str) {
		obj[c] = obj[c] ? obj[c] + 1 : 1;
	}

	for (let i = 0; i < str.length; i++) {
		if (obj[str[i]] === 1) return i;
	}

	return -1;
}