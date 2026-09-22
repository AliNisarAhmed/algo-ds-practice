function maxScore(cards: number[], k: number): number {
  const total = cards.reduce((acc, x) => acc + x, 0);
  if (k >= cards.length) {
    return total;
  }

  let state = 0;
  let maxPoints = 0;
  let start = 0;

  for (let end = 0; end < cards.length; end++) {
    state += cards[end];

    if (end - start + 1 === cards.length - k) {
      maxPoints = Math.max(maxPoints, total - state);
      state -= cards[start];
      start++;
    }
  }

  return maxPoints;
}
