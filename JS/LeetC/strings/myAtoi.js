function myAtoi(str) {
	try {
		const [factor, rest] = checkSign(str.trimLeft());
		const result = Number(factor * takeWhile(rest, isNumber));
		let minLimit = -1 * Math.pow(2, 31);
		let maxLimit = Math.pow(2, 31) - 1;
		if (result < minLimit) {
			return minLimit;
		}

		if (result > maxLimit) {
			return maxLimit;
		}

		return result;
	} catch (e) {
		return 0;
	}
}

function takeWhile(str, f) {
	let result = '';
	for (let c of str) {
		if (f(c)) {
			result += c;
		} else {
			return result;
		}
	}
	return result;
}

function isNumber(char) {
	const code = char.charCodeAt(0);
	return code >= 48 && code <= 57;
}

function checkSign(str) {
	if (str[0] === '-') {
		return [-1, str.slice(1)];
	} else if (str[0] === '+') {
		return [1, str.slice(1)];
	} else if (isNumber(str[0])) {
		return [1, str];
	} else {
		throw new Error('Invalid string');
	}
}

myAtoi('42');
