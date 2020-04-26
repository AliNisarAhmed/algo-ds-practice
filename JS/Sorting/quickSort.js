function quickSort(arr, left = 0, right = arr.length - 1) {
	if (left < right) {
		const pivotIndex = helper(arr, left, right);
		// left side
		quickSort(arr, left, pivotIndex - 1);
		// right side
		quickSort(arr, pivotIndex + 1, right);
	}
	return arr;
}

function helper(arr, start = 0, end = arr.length - 1) {
	let pivot = arr[start];
	let pivotIndex = start;
	for (let i = start + 1; i <= end; i++) {
		if (pivot > arr[i]) {
			pivotIndex++;
			[ arr[i], arr[pivotIndex] ] = [ arr[pivotIndex], arr[i] ];
		}
	}

	[ arr[start], arr[pivotIndex] ] = [ arr[pivotIndex], arr[start] ];
	return pivotIndex;
}

console.log(quickSort([9, 8, 7, 6, 5, 4, 3, 2, 1]));
