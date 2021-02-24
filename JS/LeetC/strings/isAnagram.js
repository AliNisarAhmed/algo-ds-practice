function isAnagram(str1, str2) {

	let [smaller, larger] = str1.length < str2.length ? [str1, str2] : [str2, str1];

	let obj = {};
	for (let c of smaller) {
		obj[c] = obj[c] ? obj[c] + 1 : 1;
	}

	for (let c of larger) {
		if (obj[c]) {
			obj[c] = obj[c] - 1;
		} else {
			return false;
		}
	}

	return true;
}