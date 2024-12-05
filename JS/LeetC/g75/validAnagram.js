
function isAnagram(str1, str2) {
  if (str1.length !== str2.length) {
    return false;
  }

  let obj = {};

  for (let c of str1) {
    obj[c] = obj[c] ? obj[c] + 1 : 1;
  }

  for (let c of str2) {
    if (obj[c]) {
      obj[c] = obj[c] - 1;
    } else {
      return false;
    }
  }

  return true;
}
