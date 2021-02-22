function plusOne(arr) {
	let index = arr.length - 1;

	if (arr[index] !== 9) {
		arr[index]++;
		return arr;
	}

	while (arr[index] === 9) {
		arr[index] = 0;

		if (index === 0) {
			arr.unshift(1);
			return arr;
		}

		index--;
	}

	arr[index]++;

	return arr;
}