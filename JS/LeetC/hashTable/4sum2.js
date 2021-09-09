// --- Generalized n sum count

function nSumCount(...lists) {
  let m = {};
  addToHash(lists, 0, 0);
  return countComplements(lists, Math.floor(lists.length / 2), 0);

  function addToHash(lists, i, sum) {
    if (i === Math.floor(lists.length / 2)) {
      m[sum] = m[sum] === undefined ? 1 : m[sum] + 1;
    } else {
      for (let a of lists[i]) {
        addToHash(lists, i + 1, a + sum);
      }
    }
  }

  function countComplements(lists, i, comple) {
    if (i === lists.length) {
      return m[comple] === undefined ? 0 : m[comple];
    }

    let count = 0;
    for (let a of lists[i]) {
      count += countComplements(lists, i + 1, comple - a);
    }
    return count;
  }
}

// ----------------------------------------------------------
function fourSumCount(arr1, arr2, arr3, arr4) {
  let sum1 = permSumTwoArrays(arr1, arr2);
  let res = 0;

  for (let c of arr3) {
    for (let d of arr4) {
      let comple = 0 - (c + d);
      if (sum1[comple] !== undefined) {
        res += sum1[comple];
      }
    }
  }

  return res;
}

function permSumTwoArrays(arr1, arr2) {
  let obj = {};
  for (let i = 0; i < arr1.length; i++) {
    for (let j = 0; j < arr2.length; j++) {
      let sum = arr1[i] + arr2[j];
      obj[sum] = obj[sum] ? obj[sum] + 1 : 1;
    }
  }

  return obj;
}
