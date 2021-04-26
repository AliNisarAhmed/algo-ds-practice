function fizzBuzz(n) {
	return Array.from({ length: n }, (_, i) => {
		if ((i + 1) % 3 === 0 && (i + 1) % 5 === 0) {
			return 'FizzBuzz';
		}

		if ((i + 1) % 3 === 0) {
			return 'Fizz';
		}

		if ((i + 1) % 5 === 0) {
			return 'Buzz';
		}

		return `${(i + 1)}`
	});
}
