function intersect(arr1, arr2) {
	// the idea is to get the count from the first arr in an obj
	// then iteratre through the second,
	// if the count of a number is > 0, put it in the result and decrement its count
	// if the count is zero, that number is discarded coz it has already been in the array the minimum number of times

	let smaller = arr1.length < arr2.length ? arr1 : arr2;
	let larger = arr1.length < arr2.length ? arr2 : arr1;

	const obj = {};
	let result = [];

	for (let elem of smaller) {
		obj[elem] = obj[elem] ? obj[elem] + 1 : 1;
	}

	for (let elem of larger) {
		if (obj[elem]) {
			if (obj[elem] > 0) {
				result.push(elem);
				obj[elem] = obj[elem] - 1;
			}
		}
	}

	return result;
}


// However, if the arrays are already sorted, we use two pointer approach.

function intersect(arr1, arr2) {
	arr1.sort((a, b) => a - b);
	arr2.sort((a, b) => a - b);

	let i = 0;
	let j = 0;
	let k = 0;

	let result = [];

	while (i < arr1.length && j < arr2.length) {
		if (arr1[i] < arr2[j]) {
			i++;
		} else if (arr1[i] > arr2[j]) {
			j++;
		} else {
			result[k] = arr1[i];
			k++;
			i++;
			j++;
		}
	}

	return result;
}


// my version with strictly two pointers

function intersect(arr1, arr2) {
	arr1.sort((a, b) => a - b);
	arr2.sort((a, b) => a - b);

	let i = 0;
	let j = 0;

	let result = [];

	while (i < arr1.length && j < arr2.length) {
		if (arr1[i] === arr2[j]) {
			result.push(arr1[i]);
			i++;
			j++;
		}

		else {
			if (arr1[i] > arr2[j]) {
				while (arr1[i] > arr2[j]) {
					j++;
				}
			} else {
				while (arr2[j] > arr1[i]) {
					i++;
				}
			}
		}
	}

	return result;
}