
// use reverse technique

function rotate(arr, k) {
  k = k % arr.length;
	arr.reverse();
	reverseInPlace(arr, 0, k - 1);
	reverseInPlace(arr, k);
}

function reverseInPlace(arr, start, end = arr.length - 1) {
	while (start < end) {
		[ arr[start], arr[end] ] = [ arr[end], arr[start] ]
		start++;
		end--;
	}
}

// ----------------------------------

// use an extra array to store the elements at their final positions

function rotateExtra(arr, k) {
	let tempArr = [];

	for (let i = 0; i < arr.length; i++) {
		tempArr[(i + k) % arr.length] = arr[i];
	}

	for (let i = 0; i < tempArr.length; i++) {
		arr[i] = tempArr[i];
	}
}

// ------------------------------------

// rotate once k times

function rotate(arr, k) {
	if (k >= arr.length) {
		k = k % arr.length;
	}
	while (k > 0) {
		rotate1(arr);
		k--;
	}
}

function rotate1(arr) {
	let temp = null;
	let index = 1;
	for (let i = 0; i < arr.length; i++) {
		if (temp === null) {
			temp = arr[index];
			arr[index] = arr[0];
		} else {
			[arr[index], temp] = [temp, arr[index]];
		}
		index = (index + 1) % arr.length;
	}
}

let arr = [1, 2, 3];
// rotate(arr, 4);
rotateExtra(arr, 4);
console.log(arr);
