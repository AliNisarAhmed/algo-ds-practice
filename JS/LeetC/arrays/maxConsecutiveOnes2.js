function findMaxConsecutiveOnes(arr) {
	let max = 0;
	let zeroSeen = false;
	let onesSinceLastZero = 0;
	let curr = 0;

	for (let i = 0; i < arr.length; i++) {

		let currentElem = arr[i];

		if (zeroSeen) {
			if (currentElem === 0) {
				// we found a repeating zero
				max = Math.max(max, curr);
				curr = onesSinceLastZero + 1;
				onesSinceLastZero = 0;
			} else {
				curr++;
				onesSinceLastZero++;
			}
		} else {
			if (currentElem === 0) {
				// we found first zero
				zeroSeen = true;
			}
			curr++;
		}
	}

	return Math.max(max, curr);
}