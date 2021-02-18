function getMaxProfit(stockPrices) {
	if (stockPrices.length < 2) {
		throw new Error('Need at least two prices');
	}

	let low = Infinity;
	let profit = -Infinity;

	for (let price of stockPrices) {
		if (price < low) {
			if (price - low > profit) {
				profit = price - low;
			}
			low = price;
		} else {
			if (price - low > profit) {
				profit = price - low;
			}
		}
	}

	return profit;
}

function getMaxProfit(stockPrices) {
  if (stockPrices.length < 2) {
    throw new Error('Getting a profit requires at least 2 prices');
  }

  let minPrice = stockPrices[0];
  let maxProfit = stockPrices[1] - stockPrices[0];

  for (let i = 1; i < stockPrices.length; i++) {
    const currentPrice = stockPrices[i];

    const potentialProfit = currentPrice - minPrice;

    maxProfit = Math.max(maxProfit, potentialProfit);

    minPrice = Math.min(minPrice, currentPrice);
  }

  return maxProfit;
}