function climbStairs(n: number): number {
  return climbStairsRec(n, { 1: 1, 2: 2 });
}

function climbStairsRec(n: number, memo: Record<number, number>): number {
  if (memo[n]) {
    return memo[n];
  }

  const result = climbStairsRec(n - 1, memo) + climbStairsRec(n - 2, memo);
  memo[n] = result;
  return result;
}
