function mergeArrays(arr1, arr2) {

	let result = [];

	let leftIndex = 0, rightIndex = 0;

	while (leftIndex <= arr1.length && rightIndex <= arr2.length) {

		if (leftIndex === arr1.length) {
			result.push(...arr2.slice(rightIndex));
			return result;
		}

		if (rightIndex === arr2.length) {
			result.push(...arr1.slice(leftIndex));
			return result;
		}

		let leftElem = arr1[leftIndex], rightElem = arr2[rightIndex];

		if (leftElem < rightElem) {
			result.push(leftElem);
			leftIndex++;
		} else {
			result.push(rightElem);
			rightIndex++;
		}
	}
}