function sortedSquares(arr) {
	let left = 0;
	let right = arr.length - 1;

	let result = [];

	for (let i = right; i >= 0; i--) {
		if (Math.abs(arr[right]) > Math.abs(arr[left])) {
			result[i] = arr[right] * arr[right];
			right--;
		} else {
			result[i] = arr[left] * arr[left];
			left++;
		}
	}
	return result;
}

console.log(sortedSquares([-4,-1,0,3,10]));