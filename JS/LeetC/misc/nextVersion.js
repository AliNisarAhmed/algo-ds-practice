// Comments on Time and Space Complexity:

// Time complexity os O(n)
	// This is because strings in JS are immutable, so they must be converted to an array (aka a "character" array), which is O(n)

// Space complexity is also O(n), because of the need to convert the string to an array.

function nextVersion(str) {
	// split on "." and try to convert each character to a number
	const numArr = str.split('.').map((x) => Number(x));

	// if any char could not be converted to number, the input str was not a valid version number
	if (numArr.some((x) => Number.isNaN(x))) {
		throw new Error('Invalid version number');
	}

	// increment the numArr in place
	incrementVersion(numArr);

	return numArr.join('.');
}

function incrementVersion(arr) {
	for (let i = arr.length - 1; i >= 0; i--) {
		if (arr[i] === 9) {
			if (i === 0) {
				// Numbers more than 9 are allowed as the first digit
				arr[i] += 1;
			} else {
				arr[i] = 0;
			}
		} else {
			arr[i] += 1;
			break;
		}
	}
}

console.log(nextVersion('1.2.3'));
console.log(nextVersion('0.9.9'));
console.log(nextVersion('1.2'));
console.log(nextVersion('1'));
console.log(nextVersion('1.2.3.4.5.6.7.8'));
console.log(nextVersion('9.9'));
console.log(nextVersion('1.2.a'));
