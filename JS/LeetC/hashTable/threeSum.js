
function threeSum(arr) {
  let res = [];
  let dups = new Set();
  let seen = {};

  for (let i = 0; i < arr.length; i++) {

    if (!dups.has(arr[i])) {
      dups.add(arr[i]);

      for (let j = i + 1; j < arr.length; j++) {
        let comple = 0 - arr[i] - arr[j];

        if (seen[comple] !== undefined && seen[comple] === i) {
          res.push([ arr[i], arr[j], arr[comple] ])
        }
        seen[arr[j]] = i;
      }
    }
  }

  return res;
}








// sorting allowed
function threeSum(arr) {
  arr.sort((a, b) => a - b);
  let res = [];

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
      break;
    }
    if (i === 0 || arr[i - 1] !== arr[i]) {
      twoSum2(arr, i, res);
    }
  }

  return res;
}

function twoSum2(arr, i, res) {
  let j = i + 1,
    k = arr.length - 1;

  while (j < k) {
    let sum = arr[i] + arr[j] + arr[k];
    if (sum < 0) {
      j++;
    } else if (sum > 0) {
      k--;
    } else {
      res.push([arr[i], arr[j], arr[k]]);
      j++;
      k--;

      while (j < k && arr[j] === arr[j - 1]) {
        j++;
      }
    }
  }
}
