function countBits2(n: number): number[] {
  return Array.from({ length: n + 1 }, (_, i) => i).map((k) =>
    hammingWeight(k),
  );
}

function hammingWeight(n: number): number {
  let count = 0;
  while (n !== 0) {
    count++;
    n = n & (n - 1);
  }
  return count;
}

function countBits(n: number): number[] {
  const result: number[] = [];
  result[0] = 0;
  for (let i = 1; i <= n; i++) {
    result[i] = result[i >> 1] + (i & 1);
  }
  return result;
}

console.log(countBits(5));
