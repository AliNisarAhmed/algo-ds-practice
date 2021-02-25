// Find numbers with Even number of digits

function findNumbers(nums) {
	return nums.map(numberOfDigits).filter(isEven).length;
}

function isEven(num) {
	return num % 2 === 0;
}

function numberOfDigits(num) {
	let result = 0;
	while (num > 0) {
		num = Math.floor(num / 10);
		result++;
	}

	return result;
}

findNumbers([12, 34, 5])