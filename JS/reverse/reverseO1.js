function reverse(arr) {
	let len = arr.length;
	let midpoint = Math.floor(len / 2);
	for (let i = 0; i < midpoint; i++) {
		[arr[i], arr[len - 1 - i] ] = [ arr[len - 1 - i], arr[i] ];
	}

	return arr;
}

let arr = [1, 2, 3];

console.log('arr', reverse(arr));
