function intersection(arr1, arr2) {
	let temp = {};
	let result = [];

	for (let e of arr1) {
		temp[e] = true;
	}

	for (let f of arr2) {
		if (temp[f]) {
			result.push(f);
		}
	}

	return result;
}

function findFirstDup(arr) {
	let temp = {};

	for (let e of arr) {
		if (temp[e]) {
			return e;
		} else {
			temp[e] = true;
		}
	}

	return false;
}

findFirstDup(['a', 'b', 'c', 'd', 'c', 'e', 'f', 'f']);

function findMissingAlpha(str) {
	let chars = {};

	for (let c of str) {
		chars[c] = true;
	}

	for (let e of 'abcdefghijklmnopqrstuvwxyz') {
		if (!chars[e]) {
			return e;
		}
	}
}

findMissingAlpha('the quick brown box jumps over a lazy dog');

function firstNonDup(str) {
	let chars = {};

	for (let e of str) {
		chars[e] = chars[e] ? chars[e] + 1 : 1;
	}

	for (let v of str) {
		if (chars[v] <= 1) return v;
	}
}

firstNonDup('minimum');
