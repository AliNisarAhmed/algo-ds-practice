function insertionSort(arr) {

	for (let i = 1; i < arr.length; i++) {
		let temp = arr[i];

		let position = i - 1;

		while (position >= 0) {
			if (arr[position] > temp) {
				arr[position + 1] = arr[position];
				position = position - 1;
			} else {
				break;
			}
		}

		// position + 1 here because we decrement position 1 more than necessary in the while loop
		arr[position + 1] = temp;
	}

	return arr;
}

insertionSort([4, 3, 2, 1])