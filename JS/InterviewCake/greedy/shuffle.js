function shuffle(arr) {
	for (let i = 0; i < arr.length; i++) {
		let index = getRandom(i, arr.length - 1);
		[arr[i], arr[index] ] = [ arr[index], arr[i] ];
	}
	return arr;
}

function getRandom(floor, ceil) {
	return Math.floor(Math.random() * (ceil - floor + 1) + floor);
}
