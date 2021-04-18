function validMountainArray(arr) {
	let i = 0;

	while (i < arr.length) {

		if (arr[i] >= arr[i + 1]) {
			break;
		}

		i++;
	}

	if (i === 0 || i >= arr.length) {
		return false;
	}

	while (i < arr.length) {
		if (arr[i] <= arr[i + 1]) {
			return false;
		}

		i++;
	}

	return true;
}

console.log(validMountainArray([2, 1]));