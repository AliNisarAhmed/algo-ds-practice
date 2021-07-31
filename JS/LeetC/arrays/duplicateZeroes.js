
// O(N) solution:
	// two passes
	// 1. count possible duplicate zeroes
			// make sure not counting zeroes at the edge
	// 2. start shifting from the end, shifting non zero by one, and copying zeroes

function duplicateZeros(arr) {
	let possibleDups = 0;
	let length = arr.length - 1;

	for (let left = 0; left <= length - possibleDups; left++) {

		if (arr[left] === 0) {

			// this check is necessary because elements beyond the original length of the list are not written.
			// i.e. length of the array remains the same after substitutions
			if (left === length - possibleDups) {
				arr[length] = 0;
				length--;
				break;
			}
			possibleDups++;

		}
	}

	let last = length - possibleDups;

	for (let i = last; i >= 0; i--) {
		if (arr[i] === 0) {
			arr[i + possibleDups] = 0;
			possibleDups--;
			arr[i + possibleDups] = 0;
		} else {
			arr[i + possibleDups] = arr[i];
		}
	}

}



// This is O(n^2)

// function duplicateZeros(arr) {
// 	let i = 0;
// 	while (i < arr.length - 1) {
// 		if (arr[i] === 0) {
// 			for (let j = arr.length - 2; j > i; j--) {
// 				arr[j + 1] = arr[j];
// 			}
// 			arr[i + 1] = 0;
// 			i++;
// 		}
// 		i++;
// 	}
// }


// function duplicateZeroes(arr) {
// 	let i = 0;
// 	let j = orignalLength = arr.length;
// 	while (i < j) {
// 		if (arr[i] === 0) {
// 			arr.splice(i, 0, 0);
// 			i = i + 2;
// 			j++;
// 		} else {
// 			i++;
// 		}
// 	}
// 	arr.length = orignalLength;
// }

let arr = [1,0,2,3,0,4,5,0];

duplicateZeros(arr);

console.log(arr);