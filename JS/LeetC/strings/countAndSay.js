function countAndSay(n) {
	return say(1, '1', n);
}

function say(current, acc, max) {
	if (current >= max) {
		return acc;
	}

	return say(current + 1, count(acc), max);
}

function count(n) {
	let i = 0;
	let acc = '';
	while (i < n.length) {
		let count = 1;
		while (n[i] === n[i+1]) {
			count++;
			i++;
		}

		i++;
		acc = acc + `${count}${n[i - 1]}`;
	}
	return acc;
}

console.log(countAndSay(3));