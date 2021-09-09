// Input array is sorted 
//
//
// we can now use a two pointer approach

function twoSum (arr, target) {
  let i = 0; 
  let j = arr.length - 1;
  let res = 0;

  while (i < j) {
    let sum = arr[i] + arr[j];

    if (sum === target) {
      return [i + 1, j + 1];
    } else if (sum > target) {
      j--;
    } else {
      i++;
    }
  }

  return [-1, -1]
}
