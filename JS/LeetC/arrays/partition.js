// Method 1
//
////1. The left pointer continuously moves one cell to the right until it reaches
//a value that is greater than or equal to the pivot, and then stops.
//2. Then, the right pointer continuously moves one cell to the left until it
//reaches a value that is less than or equal to the pivot, and then stops.
//The right pointer will also stop if it reaches the beginning of the array.
//3. Once the right pointer has stopped, we reach a crossroads. If the left
//pointer has reached (or gone beyond) the right pointer, we move on to
//Step 4. Otherwise, we swap the values that the left and right pointers are
//pointing to, and then go back to repeat Steps 1, 2, and 3 again.
//4. Finally, we swap the pivot with the value that the left pointer is currently
// pointing to.

function partition(arr, leftPointer = 0, rightPointer = arr.length - 1) {
  let pivotIndex = rightPointer;

  let pivot = arr[rightPointer];

  rightPointer -= 1;

  while (true) {
    while (arr[leftPointer] < pivot) {
      leftPointer++;
    }

    while (arr[rightPointer] > pivot) {
      rightPointer--;
    }

    if (leftPointer >= rightPointer) {
      break;
    }

    [arr[leftPointer], arr[rightPointer]] = [
      arr[rightPointer],
      arr[leftPointer],
    ];

    leftPointer++;
  }

  [arr[leftPointer], arr[pivotIndex]] = [arr[pivotIndex], arr[leftPointer]];

  return leftPointer;
}
