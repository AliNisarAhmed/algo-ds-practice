const values = {
  I: 1,
  V: 5,
  X: 10,
  L: 50,
  C: 100,
  D: 500,
  M: 1000,
  IV: 4,
  IX: 9,
  XL: 40,
  XC: 90,
  CD: 400,
  CM: 900
}
function romanToInt(s) {
  let i = 0;
  let sum = 0;
  while (i < s.length) {
    const current = s[i];
    const next = s[i + 1];

    if (!next) {
      sum += values[current];
      i++;
    } else {
      if (values[`${current}${next}`]) {
        sum += values[`${current}${next}`];
        i += 2;
      } else {
        sum += values[current];
        i += 1;
      }
    }
  }

  return sum;
}
