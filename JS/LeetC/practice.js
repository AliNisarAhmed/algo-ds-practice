function moveZeroes(arr) {
	let zeroIndex = arr.findIndex(v => v === 0);
	if (zerIndex < 0) return;

	let nonZeroIndex = zeroIndex;

	while (arr[nonZeroIndex] === 0) {
		nonZeroIndex++;
	}

	[ arr[zeroIndex], arr[nonZeroIndex] ] = [arr[nonZeroIndex], arr[zeroIndex]];


}






















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