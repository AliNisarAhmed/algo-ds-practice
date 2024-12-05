import { letterFreq } from "./freq";

function palindromePermutation(str: string): boolean {
  const freq: Record<string, number> = letterFreq(str);
  let isOdd = false;
  for (let [char, count] of Object.entries(freq)) {
    if (count % 2 !== 0) {
      if (isOdd) {
        return false;
      }

      isOdd = true;
    }
  }

  return true;
}

console.log(palindromePermutation("Tact CoaTT"));
