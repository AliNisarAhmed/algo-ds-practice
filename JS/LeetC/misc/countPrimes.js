function countPrimes(n) {
	let isPrime = Array.from({ length: n }, (_) => true);

	for (let i = 2; i * i < n; i++) {
		if (isPrime[i]) {
			for (let j = i * i; j < n; j += i) {
				isPrime[j] = false;
			}
		}
	}

	return isPrime.slice(2).filter(Boolean).length;
}
