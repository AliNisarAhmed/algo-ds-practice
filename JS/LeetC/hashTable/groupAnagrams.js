// associate every character with a unique prime aka Godel encoding
// then the product of characters for each anagram will be unqiue

const primes = {
  a: 2,
  b: 3,
  c: 5,
  d: 7,
  e: 11,
  f: 13,
  g: 17,
  h: 19,
  i: 23,
  j: 29,
  k: 31,
  l: 37,
  m: 41,
  n: 43,
  o: 47,
  p: 53,
  q: 59,
  r: 61,
  s: 67,
  t: 71,
  u: 73,
  v: 79,
  w: 83,
  x: 89,
  y: 97,
  z: 101,
};

function groupAnagrams(arr) {

  let obj = {};
  let res = [];

  for (let str of arr) {
    let key = generateKey(str);

    if (obj[key] !== undefined) {
      obj[key].push(str);
    } else {
      obj[key] = [str];
    }
  }

  for (let [_, val] of Object.entries(obj)) {
    res.push(val);
  }

  return res;
}

function generateKey(str) {
  let prod = 1;

  for (let c of str) {
    prod *= primes[c];
  }

  return prod;
}


