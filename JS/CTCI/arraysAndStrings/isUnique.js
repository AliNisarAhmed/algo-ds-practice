function isUnique(str) {
  // assuming the string consists of lower case english letters
  let checker = 0;
  for (let index of [...str].map((c) => c.charCodeAt() - "a".charCodeAt())) {
    const mask = 1 << index;
    if (checker & mask) {
      return false;
    }
    checker = checker | mask;
  }

  return true;
}
