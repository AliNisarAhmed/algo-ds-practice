function convertFromBase(str, base) {
	if (base < 2 || (base > 10 && base !== 16)) return -1;

	let value = 0;

	for (let i = str.length - 1; i >= 0; i--) {
		let digit = parseInt(str[i], base);
		if (digit < 0 || digit >= base || Number.isNaN(digit)) {
			return -1;
		}

		let exp = str.length - 1 - i;

		value += digit * Math.pow(base, exp);

	}

	return value;
}


console.log(convertFromBase('1000', 2));