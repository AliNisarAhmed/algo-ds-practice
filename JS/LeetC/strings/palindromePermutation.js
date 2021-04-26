function palindromePermutation(str) {
	let charCountMap = getCharCountMap(str);


	return checkIfPalindrome(charCountMap);
}

function checkIfPalindrome(charCountMap) {
	let hasOdd = false;

	for (let v of Object.values(charCountMap)) {
		if (v % 2 !== 0) {
			if (hasOdd) {
				return false;
			}

			hasOdd = true;
		}
	}

	return true;
}

function getCharCountMap(str) {
	let result = {};
	for (let c of str) {
		if (c.trim().length > 0) {
			result[c] = result[c] ? result[c] + 1 : 1;
		}
	}

	return result;
}

console.log(palindromePermutation('atco cta'));