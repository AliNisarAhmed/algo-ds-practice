const values: Record<string, number> = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
};

function romanToInt(s: string): number {
  let total = 0;
  for (let i = s.length - 1; i >= 0; i--) {
    const current = values[s[i]];
    const prev = values[s[i + 1]];

    if (prev && current < prev) {
      total -= current;
    } else {
      total += current;
    }
  }

  return total;
}
