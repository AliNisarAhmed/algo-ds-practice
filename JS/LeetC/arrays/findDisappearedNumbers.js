// compared to the second solution below where we set found elements to -1, this one just reverses the signs of all the seen indices.

function findDisappearedNumbers(arr) {
	for (let i = 0; i < arr.length; i++) {
		let index = Math.abs(arr[i]) - 1;
		if (arr[index] > 0) {
			arr[index] = arr[index] * -1;
		}
	}

	let result = [];

	for (let i = 0; i < arr.length; i++) {
		if (arr[i] > 0) {
			result.push(i + 1);
		}
	}

	return result;
}

// using the given array, any number we encounter in it we set the value at that (number - 1) index to be -1. We also keep track of the number being replaced and continue replacing them as well with -1;

// function findDisappearedNumbers(arr) {
// 	for (let i = 0; i < arr.length; i++) {
// 		if (arr[i] === -1) {
// 			continue;
// 		}

// 		let index = arr[i] - 1;
// 		let toBeReplaced = null;

// 		if (arr[index] !== -1) {
// 			toBeReplaced = arr[index] - 1;
// 		}

// 		arr[index] = -1;

// 		while (toBeReplaced !== null && arr[toBeReplaced] !== -1) {
// 			let temp = arr[toBeReplaced] - 1;
// 			arr[toBeReplaced] = -1;
// 			toBeReplaced = temp;
// 		}
// 	}

// 	let result = [];

// 	for (let i = 0; i < arr.length; i++) {
// 		if (arr[i] !== -1) {
// 			result.push(i + 1);
// 		}
// 	}

// 	return result;
// }

console.log(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]));
// console.log(findDisappearedNumbers([2, 3, 4, 5, 6, 7, 8, 1]));
