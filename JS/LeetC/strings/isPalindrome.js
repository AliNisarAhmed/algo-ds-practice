function isPalindrome(str) {
	let i = 0, j = str.length - 1;

	while (i < j) {
		const l = str[i];
		const r = str[j];

		if (!isAlpha(l)) {
			i++;
		} else if (!isAlpha(r)) {
			j--;
		} else {
			if (l.toLowerCase() !== r.toLowerCase()) {
				return false;
			}
			i++;
			j--;
		}
	}
	return true;
}

// function isPalindrome(str) {
// 	const filtered = filterNonAlpha(str);
// 	let i = 0,
// 		j = filtered.length - 1;
// 	while (i < j) {
// 		if (filtered[i] !== filtered[j]) {
// 			return false;
// 		}

// 		i++;
// 		j--;
// 	}

// 	return true;
// }

// function filterNonAlpha(str) {
// 	let result = '';
// 	for (let c of str) {
// 		if (isAlpha(c)) {
// 			result = result + c.toLowerCase();
// 		}
// 	}
// 	return result;
// }

function isAlpha(c) {
	const charCode = c.charCodeAt(0);
	return (
		(charCode >= 65 && charCode <= 90) ||
		(charCode >= 97 && charCode <= 122) ||
		(charCode >= 48 && charCode <= 57)
	);
}

isPalindrome('A man, a plan, a canal: Panama');
