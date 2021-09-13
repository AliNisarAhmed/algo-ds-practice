function quickSelect(
  arr,
  kthLowest,
  leftIndex = 0,
  rightIndex = arr.length - 1
) {
  // if we reach a base case, i.e, the subarray has one cell,
  // we know we've found the value we're looking for
  if (rightIndex - leftIndex <= 0) {
    return arr[leftIndex];
  }

  let pivotIndex = partition(arr, leftIndex, rightIndex);

  if (kthLowest < pivotIndex) {
    quickSelect(arr, kthLowest, leftIndex, pivotIndex - 1);
  } else if (kthLowest > pivotIndex) {
    quickSelect(arr, kthLowest, pivotIndex + 1, rightIndex);
  } else {
    return arr[pivotIndex];
  }
}

// 2nd to lowest -> quickSelect(arr, 1)
