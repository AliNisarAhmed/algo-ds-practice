function thirdMax(arr, k = 3) {
	let set = new Set();

	for (let e of arr) {
		set.add(e);
		if (set.size > k) {
			set.delete(Math.min(...set));
		}
	}

	if (set.size === k) {
		return Math.min(...set);
	}

	return Math.max(...set);
}

// function thirdMax(arr) {
// 	let m1 = Number.NEGATIVE_INFINITY;
// 	let m2 = Number.NEGATIVE_INFINITY;
// 	let m3 = Number.NEGATIVE_INFINITY;

// 	for (let e of arr) {
// 		if (e > m1) {
// 			m3 = m2;
// 			m2 = m1;
// 			m1 = e;
// 		} else if (e < m1 && e > m2) {
// 			m3 = m2;
// 			m2 = e;
// 		} else if (e < m2 && e > m3) {
// 			m3 = e;
// 		}
// 	}

// 	return m3 !== Number.NEGATIVE_INFINITY ? m3 : m1;
// }

console.log(thirdMax([3, 2, 1]));
