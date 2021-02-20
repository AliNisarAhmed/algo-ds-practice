function getProductsOfAllIntsExceptAtIndex(arr) {

	if (arr.length <= 1) return arr;

	let result = [arr[0]];
	let temp = 1;

	for (let i = 1; i < arr.length; i++) {
		result[i] = temp * arr[i - 1];
		temp = result[i] * temp;
	}

	temp = arr[arr.length - 1];

	for (let i = arr.length - 2; i >= 0; i--) {
		result[i] = result[i] * temp;
		temp = arr[i] * temp;
	}

	return result;
}

console.log(getProductsOfAllIntsExceptAtIndex([]));



