function longestPalindrome(s: string): number {
  let count = 0;
  const set = new Set<string>();

  for (let c of s) {
    if (set.has(c)) {
      count += 2;
      set.delete(c);
    } else {
      set.add(c);
    }
  }

  return set.size > 0 ? count + 1 : count;
}
