function quickSort(arr, leftPointer = 0, rightPointer = arr.length - 1) {
  // base case, the subarray has 0 or 1 elements
  if (rightPointer - leftPointer <= 0) {
    return;
  }

  // for partition algo, see partition.js
  let pivotIndex = partition(arr, leftPointer, rightPointer);

  quickSort(leftPointer, pivotIndex - 1);

  quickSort(pivotIndex + 1, rightPointer);
}
