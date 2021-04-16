function maxProfit(prices) {

	if (prices.length === 0) {
		return 0;
	}

	let i = 0;
	let j = 1;
	let profit = prices[j] - prices[i];

	while (j < prices.length) {
		if (prices[j] < prices[i]) {
			// found a new minumum
			i = j;
			j = i + 1;
		} else if (prices[j] - prices[i] > profit) {
      // found greater profit
			profit = prices[j] - prices[i];
			j++;
		} else {
			j++;
		}
	}

	return profit > 0 ? profit : 0;
}

console.log(maxProfit([2, 1, 4]));
