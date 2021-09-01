function numJewelsInStones(jewels, stones) {
  let obj = {};

  for (let c of jewels) {
    obj[c] = true;
  }

  let count = 0;

  for (let c of stones) {
    if (obj[c]) {
      count++;
    }
  }

  return count;
}
