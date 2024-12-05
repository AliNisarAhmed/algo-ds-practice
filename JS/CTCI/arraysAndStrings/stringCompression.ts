function stringCompression2(str: string): string {
  const result: string[] = [];
  let i = 0;
  while (i < str.length) {
    let current = str[i];
    let currentCount = 1;
    let j = i;
    while (j < str.length && str[j] === str[j + 1]) {
      currentCount += 1;
      j++;
    }
    result.push(`${current}${currentCount}`);
    i = j + 1;
  }

  return result.join("");
}

function stringCompression(str: string): string {
  const compressedCount = countCompressed(str);
  if (compressedCount >= str.length) {
    return str;
  }

  return stringCompression2(str);
}

function countCompressed(str: string): number {
  let i = 0;
  let result = 0;
  while (i < str.length) {
    result++;

    while (str[i] === str[i + 1]) {
      i++;
    }

    i++;
  }

  return result * 2;
}

console.log(stringCompression("aaaaaa"));
