function checkIfExist(arr) {
	for (let i = 0; i < arr.length; i++) {
		for (let j = i + 1; j < arr.length; j++) {
			if (arr[i] === 2 * arr[j] || arr[j] === 2 * arr[i]) {
				return true;
			}
		}
	}

	return false;
}

function checkIfExist(arr) {
	let obj = {};

	for (let i = 0; i < arr.length; i++) {
		if (obj[arr[i] * 2]) {
			return true;
		} else if (arr[i] % 2 === 0 && obj[arr[i] / 2]) {
			return true;
		}

		obj[arr[i]] = true;
	}

	return false;
}

console.log(checkIfExist([-2, 0, 10, -19, 4, 6, -8]));