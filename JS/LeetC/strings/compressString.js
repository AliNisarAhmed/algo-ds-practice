function compress(str) {
	let arr = [...str];

	let uniqueChars = removeDups(arr);

	console.log(uniqueChars);

	if (uniqueChars === str) {
		return str;
	}

	return appendCounts(str);
}

function appendCounts(str) {
	let i = 0;
	let current = str[i];
	let result = [];

	while (i < str.length) {
		result.push(str[i]);
		let count = 0;

		while (str[i] === current) {
			i++;
			count++;
		}

		result.push(count);
		current = str[i];
	}

	return result.join('');
}

function removeDups(arr) {
	let i = 0;
	let current = arr[i];

	let result = [];

	while (i < arr.length) {
		result.push(current);

		while (arr[i] === current) {
			i++;
		}

		current = arr[i];
	}

	return result;
}


console.log(compress('aabcccccaaa'));