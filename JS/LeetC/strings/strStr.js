function strStr(haystack, needle) {
	if (needle.length === 0) return 0;
	if (needle.length > haystack.length) return -1;

	const needleHash = calculateHash(needle);
	const initialHaystackHash = calculateHash(haystack.slice(0, needle.length));

	if (needleHash === initialHaystackHash) {
		return 0;
	}

	let h = initialHaystackHash;
	const aL = Math.pow(26, needle.length); // a ^ L
	// aL could be large, but in JS since integers are 64 bit we don't have to worry abouyt overflow, but for 32 bit ints we must check if it ever exceed 2^31

	for (let i = 1; i < haystack.length - needle.length + 1; i++) {
		let previous = charToIntMod26(haystack[i - 1]);
		let next = charToIntMod26(haystack[i - 1 + needle.length]);
		h = (h * 26 - previous * aL) + next;
		if (h === needleHash) {
			return i;
		}
	}

	return -1;
}

function calculateHash(str) {
	return [...str].reduce(
		(acc, c, i) => acc + charToIntMod26(c) * Math.pow(26, str.length - i - 1),
		0
	);
}

function charToIntMod26(c) {
	return c.charCodeAt(0) - 'a'.charCodeAt(0);
}

// --------------------------------------------

// function strStr(haystack, needle) {

// 	let L = needle.length;
// 	let n = haystack.length;

// 	if (L === 0) return 0;

// 	let pn = 0;

// 	while (pn < n - L + 1) {
// 		while (pn < n - L + 1 && haystack[pn] !== needle[0]) {
// 			pn++;
// 		}

// 		let currentLength = 0;
// 		let pl = 0;

// 		while (pl < L && pn < n && haystack[pn] === needle[pl]) {
// 			pn++;
// 			pl++;
// 			currentLength++;
// 		}

// 		if (currentLength === L) {
// 			return pn - L;
// 		}

// 		pn = pn - currentLength + 1;
// 	}

// 	return -1;
// }

// function strStr(haystack, needle) {
// 	if (needle.length === 0) return 0;

// 	for (let i = 0; i <= haystack.length - needle.length; i++) {
// 		let sub = haystack.substring(i, i + needle.length);
// 		if (sub === needle) {
// 			return i;
// 		}
// 	}

// 	return -1;
// }

// console.log(strStr('mississippi', 'pi'));
// console.log(strStr('mississippi', 'issip'));
// console.log(strStr('wxyzabcd', 'abcd'));
console.log(strStr('', 'a'));
