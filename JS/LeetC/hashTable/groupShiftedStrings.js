function groupStrings(arr) {
  let obj = {};

  for (let s of arr) {
    let key = generateKey(s);

    if (obj[key] !== undefined) {
      obj[key].push(s);
    } else {
      obj[key] = [s];
    }
  }

  let res = [];

  for (let val of Object.values(obj)) {
    res.push(val);
  }

  return res;
}

function generateKey(str) {
  let res = [];

  for (let i = 1; i < str.length; i++) {
    let diff = charCode(str[i]) - charCode(str[i - 1]);
    if (diff < 0) {
      diff += 26;
    }
    res.push(diff);
  }

  return res.join(",");
}

function charCode(c) {
  return c.codePointAt() - 97;
}
