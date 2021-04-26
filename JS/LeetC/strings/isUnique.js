function isUnique(str) {
	const freqMap = {};

	for (let e of str) {
		freqMap[e] = freqMap[e] ? freqMap[e] + 1 : 1;
	}

	for (let v of Object.values(freqMap)) {
		if (v > 1) {
			return false;
		}
	}

	return true;
}

console.log(isUnique('abcdefa'));
