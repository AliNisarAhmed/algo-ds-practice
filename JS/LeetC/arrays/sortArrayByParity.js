const isEven = (n) => n % 2 === 0;
const isOdd = (n) => !isEven(n);

function sortArrayByParity(arr) {
	let evenP = 0;
	let oddP = arr.length - 1;

	while (evenP < oddP) {
		while (evenP < arr.length && isEven(arr[evenP])) {
			evenP++;
		}

		while (oddP > 0 && isOdd(arr[oddP])) {
			oddP--;
		}

		if (evenP < oddP) {
			// swap
			[arr[evenP], arr[oddP]] = [arr[oddP], arr[evenP]];

			evenP++;
			oddP--;
		}
	}

	return arr;
}

console.log(sortArrayByParity([0, 2]));
