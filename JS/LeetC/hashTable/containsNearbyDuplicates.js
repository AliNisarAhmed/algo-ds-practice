function containsNearbyDuplicate(arr, k) {
  let obj = {};

  for (let [i, s] of arr.entries()) {
    if (obj[s] === undefined) {
      obj[s] = i;
    } else {
      if (Math.abs(obj[s] - i) <= k) {
        return true;
      } else {
        obj[s] = i;
      }
    }
  }

  return false;
}
