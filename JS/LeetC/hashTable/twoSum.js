function twoSum(arr, target) {
  
  let obj = {};

  for (let [i, v] of arr.entries()) {

    if (obj[target - v] !== undefined) {
      return [obj[target - v], i];
    }

    obj[v] = i;
  }
}

