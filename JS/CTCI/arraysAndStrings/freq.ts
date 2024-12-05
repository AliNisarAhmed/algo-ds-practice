export function letterFreq(str: string): Record<string, number> {
  const result = {};
  for (let c of str.toLowerCase()) {
    if (c !== ' ') {
      result[c] = result[c] ? result[c] + 1: 1;
    }
  }

  return result;
}
