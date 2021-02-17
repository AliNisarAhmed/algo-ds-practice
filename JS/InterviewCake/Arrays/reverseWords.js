function reverseWords(arr) {
	arr.reverse();

	let spaceIndex = -1;
	let index = 0;

	while (index < arr.length) {

		let c = arr[index];

		if (index === arr.length - 1) {
			reverseChars(arr, spaceIndex + 1, index);
		}


		else if (c === ' ') {
			reverseChars(arr, spaceIndex + 1, index - 1);
      spaceIndex = index;
		}

		index++;

	}

  return arr;
}

function reverseChars(arr, start, end) {
	while (start < end) {
		[ arr[start], arr[end] ] = [ arr[end], arr[start] ];
		start++;
		end--;
	}
}
