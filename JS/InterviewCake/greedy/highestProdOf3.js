function highestProductOf3(arr) {
	let hp3 = arr[0] * arr[1] * arr[2];
	let hp2 = arr[0] * arr[1];
	let h = Math.max(arr[0], arr[1]);
	let lp2 = arr[0] * arr[1];
	let l = Math.min(arr[0], arr[1]);

	for (let i = 2; i < arr.length; i++) {
		let current = arr[i];

		hp3 = Math.max(hp3, current * hp2, current * lp2);

		hp2 = Math.max(hp2, current * h, current * l);

		lp2 = Math.min(lp2, current * h, current * l);

		h = Math.max(current, h);

		l = Math.min(current, l);
	}

	return hp3;
}

function highestProductOf3(arr) {
	let h1 = Math.max(arr[0], arr[1]);
	let h2 = Math.min(arr[0], arr[1]);
	let h3 = arr[2];

	let l1 = Math.min(arr[0], arr[1])
	let l2 = Math.max(arr[0], arr[1])

	for (let i = 3; i < arr.length; i++) {
		let current = arr[i];

		[h1, h2, h3] = getTopThree(h1, h2, h3, current);
		[l1, l2] = getLowest2(l1, l2, current);
	}

	let h = h1 * h2 * h3;
	let l = h1 * l1 * l2;
	return h > l ? h : l;

}

function getTopThree(h1, h2, h3, current) {
	return [h1, h2, h3, current].sort((a, b) => b - a);
}

function getLowest2(l1, l2, current) {
	return [l1, l2, current].sort((a, b) => a - b);
}

highestProductOf3([-10, 1, 3, 2, -10]);