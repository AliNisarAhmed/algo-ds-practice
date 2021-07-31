// O(n) solution - use ordered histogram technique

// Since we know that heights will be in [1, 100] range, we can generate an ordered histogram (using an array) of the count of each number (value at arr[i] is the count of i in original array).
// now when we loop through the heights array, we check if each element has already been encountered based on its remainder count.
function heightChecker(arr) {
	let map = Array.from({ length: 101 }, (_) => 0);

	for (let e of arr) {
		map[e]++;
	}

	let count = 0;

	let hPtr = 1;

	for (let h of arr) {
		while (map[hPtr] === 0) {
			hPtr++;
		}

		if (h !== hPtr) {
			count++;
		}

		map[hPtr]--;
	}

	return count;
}


// O(nlogn) solution - sort and compare

// function heightChecker(arr) {
// 	let copy = arr.slice().sort((a, b) => a - b);

// 	let count = 0;

// 	for (let i = 0; i < arr.length; i++) {
// 		if (arr[i] !== copy[i]) {
// 			count++;
// 		}
// 	}

// 	return count;
// }


// console.log(heightChecker([1, 1, 4, 2, 1, 3]));
// console.log(heightChecker([5,1,2,3,4]));
console.log(heightChecker([1,2,3,4,5]));