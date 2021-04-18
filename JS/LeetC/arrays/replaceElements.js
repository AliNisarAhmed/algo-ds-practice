function replaceElements(arr) {
	let maxSoFar = -1;
	for (let i = arr.length - 1; i >= 0; i--) {
		let temp = arr[i];
		arr[i] = maxSoFar;
		maxSoFar = Math.max(maxSoFar, temp);
	}

	return arr;
}
