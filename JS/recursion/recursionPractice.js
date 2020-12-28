function numChars([first, ...rest]) {
	if (rest.length === 0) return first.length;
	return first.length + numChars(rest);
}

numChars(['ab', 'c', 'def', 'ghij']);

function even([first, ...rest]) {
	if (rest.length === 0) {
		if (first % 2 === 0) {
			return [first];
		} else {
			return [];
		}
	}

	let rem = even(rest);

	if (first % 2 === 0) {
		return [first].concat(rem);
	} else {
		return rem;
	}
}

even([1, 2, 3, 4, 5, 6]);

function triangularNum(n) {
	if (n === 1) return 1;
	return n + triangularNum(n - 1);
}

triangularNum(10);

function firstX(str) {
	return firstX2(str, 0);

	function firstX2(str, index) {
		if (str[0] === 'x') return index;

		return firstX2(str.substring(1), index + 1);
	}
}

function uniquePaths(rows, cols) {
	if (rows === 1) return 1;
	if (cols === 1) return 1;

	return uniquePaths(rows - 1, cols) + uniquePaths(rows, cols - 1);
}
