function oneAway(s1, s2) {
	if (s1.length === s2.length) {
		return oneReplaceCheck(s1, s2);
	} else if (s1.length === s2.length + 1) {
		return oneInsertCheck(s1, s2);
	} else if (s2.length === s1.length + 1) {
		return oneInsertCheck(s2, s1);
	}

	return false;
}

function oneReplaceCheck(s1, s2) {
	let foundDiff = false;

	for (let i = 0; i < s1.length; i++) {
		if (s1[i] !== s2[i]) {
			if (foundDiff) {
				return false;
			}

			foundDiff = true;
		}
	}

	return true;
}

function oneInsertCheck(s1, s2) {
	// s1 is 1 character longer than s2;

	let i1 = 0;
	let i2 = 0;

	while (i1 < s1.length && i2 < s2.length) {
		if (s1[i1] !== s2[i2]) {
			if (i1 !== i2) {
				return false;
			}
			i1++;
		} else {
			i1++;
			i2++;
		}
	}

	return true;
}

console.log(oneAway('pale', 'ple'))