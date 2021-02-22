// In place

function moveZeroes(arr) {
	let zeroIndex = arr.findIndex(e => e === 0);
	let pos = findIndexAfter(arr, zeroIndex, notZero);

	if (zeroIndex === -1 || pos === -1) return;

	while (zeroIndex < arr.length && pos < arr.length && zeroIndex < pos) {

			[ arr[pos], arr[zeroIndex] ] = [ arr[zeroIndex], arr[pos] ];

			while (zeroIndex < arr.length && arr[zeroIndex] !== 0) {
				zeroIndex++;
			}

			pos = findIndexAfter(arr, zeroIndex, notZero)
	}
}

function notZero(n) {
	return n !== 0;
}

function findIndexAfter(arr, i, pred) {
	if (i < 0 || i >= arr.length) return -1;

	for (let j = i + 1; j < arr.length; j++) {
		if (pred(arr[j])) {
			return j;
		}
	}

	return -1;
}

let arr = [0, 0, 0, 0, 0, 0 ,0,1];
console.log(moveZeroes(arr));
console.log(arr);

// Creates a new array

// function moveZeroes(arr) {
// 	let [ zeroes, nonzeroes ] = partition(arr, e => e === 0);

// 	return [...nonzeroes, ...zeroes];
// }

// function partition(arr, f) {
// 	let result = [[], []];
// 	for (let elem of arr) {
// 		if (f(elem)) {
// 			result[0].push(elem);
// 		} else {
// 			result[1].push(elem);
// 		}
// 	}

// 	return result;
// }