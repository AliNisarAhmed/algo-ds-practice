function urlify(str) {
	let charArray = [...str.trim()];

	console.log(charArray);

	for (let i = str.length - 1; i >= 0; i--) {
		if (charArray[i] === ' ') {
			charArray.splice(i, 1, '%20');
		}
	}
	console.log(charArray);

	return charArray.join('');
}

console.log(urlify('Mr John Smith    '));
