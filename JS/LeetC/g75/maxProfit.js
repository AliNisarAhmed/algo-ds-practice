function maxProfit(prices) {
  if (prices.length === 0) {
    return 0;
  }

  let i = 0;
  let j = 1;
  let profit = prices[j] - prices[i];

  while (j < prices.length) {
    if (prices[j] < prices[i]) {
      // found a new minimum
      i = j;
      j = i + 1;
    } else if (prices[j] - prices[i] > profit) {
      // found new max profit
      profit = prices[j] - prices[i];
      j++;
    } else {
      j++;
    }
  }

  return Math.max(profit, 0);
}
