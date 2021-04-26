function checkPermutation(s1, s2) {
	if (s1.length !== s2.length) return false;

	let mapString1 = {};
	let mapString2 = {};

	for (let c of s1) {
		mapString1[c] = mapString1[c] ? mapString1[c] + 1 : 1;
	}

	for (let c of s2) {
		mapString2[c] = mapString2[c] ? mapString2[c] + 1 : 1;
	}

	for (let k of Object.keys(mapString1)) {
		if (!mapString2[k] || mapString2[k] !== mapString1[k]) {
			return false;
		}
	}

	return true;
}

console.log(checkPermutation('abc', 'bcc'));