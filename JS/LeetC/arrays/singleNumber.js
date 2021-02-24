function singleNumber(arr) {
	const set = new Set();

	for (let elem of arr) {
		if (set.has(elem)) {
			set.delete(elem);
		} else {
			set.add(elem);
		}
	}

	for (let item of set.values()) {
		return item;
	}
}

// using the math formula 2 * (a + b + c) - (a + a + b + b + c) = 2c - c = c

function singleNumber(arr) {
	const set = Array.from(new Set(arr));

	return 2 * sum(set) - sum(arr);
}

function sum(arr) {
	return arr.reduce((acc, x) => acc + x);
}