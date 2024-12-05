function longestCommonPrefix(strings: string[]): string {
  const result: string[] = [];
  const minStringLength = findMinStringLength(strings);

  for (let i = 0; i < minStringLength; i++) {
    const current = strings[0][i];

    for (let j = 1; j < strings.length; j++) {
      if (strings[j][i] !== current) {
        return result.join("");
      }
    }
    result.push(current);
  }
  return result.join("");
}

function findMinStringLength(strings: string[]): number {
  let min = Number.POSITIVE_INFINITY;
  strings.forEach((s) => {
    if (s.length < min) {
      min = s.length;
    }
  });

  return min;
}

console.log(longestCommonPrefix(["flower", "flow", "flight"]));
