function oneAway2(str1: string, str2: string): boolean {
  if (Math.abs(str1.length - str2.length) > 1) {
    return false;
  }

  const freq = {};
  
  for (let c of str1) {
    freq[c] = freq[c] ? freq[c] + 1: 1;
  }

  for (let c of str2) {
    freq[c] = freq[c] ? freq[c] - 1: 1;
  }

  return Object.values(freq).filter((v) => v === 1).length <= 2;
}

function oneAway(str1: string, str2: string): boolean {
  if (Math.abs(str1.length - str2.length) > 1) {
    return false;
  }

  const s1 = str1.length < str2.length ? str1: str2; // shorter string
  const s2 = str1.length < str2.length ? str2 : str1;  // longer string

  let index1 = 0; // shorter string index
  let index2 = 0; // longer string index

  let differenceFound = false;

  while (index1 < s1.length && index2 < s2.length) {
    if (s1[index1] !== s2[index2]) {
      if (differenceFound) {
        return false;
      }
      differenceFound = true;
      if (s1.length === s2.length) {
        index1++;
      }
    } else {
      index1++;
    }
    index2++;
  }
  return true;
}

console.log(oneAway('pale', 'ple'));
console.log(oneAway('pales', 'pale'));
console.log(oneAway('pale', 'bale'));
console.log(oneAway('pale', 'bake'));
