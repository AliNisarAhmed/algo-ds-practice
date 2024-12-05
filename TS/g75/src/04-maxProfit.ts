export function maxProfit(prices: number[]): number {
  if (prices.length === 0) {
    return 0;
  }

  let i = 0;
  let j = 1;
  let profit = Number.NEGATIVE_INFINITY;

  while (j < prices.length) {
    if (prices[j] < prices[i]) {
      // found new min
      i = j;
      j = i + 1;
    } else if (profit < prices[j] - prices[i]) {
      // found new max profit
      profit = prices[j] - prices[i];
      j++;
    } else {
      j++;
    }
  }

  return Math.max(profit, 0);
}
