function containsDuplicate(arr) {
	let obj = {};
	for (let elem of arr) {
		if (obj[elem]) {
			return true;
		}

		obj[elem] = true;
	}

	return false;
}

function containsDuplicate(arr) {
	arr.sort((a, b) => a - b);

	for (let i = 0; i < arr.length - 1; i++) {
		if (arr[i] === arr[i + 1]) {
			return true;
		}
	}

	return false;
}

function containsDuplicate(arr) {
	let set = new Set(arr);
	return set.size < arr.length;
}