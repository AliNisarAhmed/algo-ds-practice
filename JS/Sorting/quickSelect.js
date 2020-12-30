// find the value at kth lowest position if the array were to be sorted
// (after sort, smallest would be at 0th position, and largest would be at (array length - 1)th position)
function quickSelect(arr, k, leftIndex = 0, rightIndex = arr.length - 1) {
	if (rightIndex - leftIndex <= 0) {
		return arr[leftIndex];
	}

	let pivotIndex = partition(arr, leftIndex, rightIndex);

	if (k < pivotIndex) {
		return quickSelect(arr, k, leftIndex, pivotIndex - 1);
	} else if (k > pivotIndex) {
		return quickSelect(arr, k, pivotIndex + 1, rightIndex);
	} else {
		return arr[pivotIndex];
	}
}

quickSelect([0, 50, 20, 10, 60, 30], 1);  // 10



// ---- partition ----

function partition(arr, leftPointer, rightPointer) {
	let pivotIndex = rightPointer;
	// choose the last element as the pivot
	let pivot = arr[rightPointer];

	// move the right pointer one left of the pivot and start the main loop
	rightPointer -= 1;


    // main loop
    while (true) {

			// stop left pointer as soon as we find an "out of place" element (i.e. >= pivot for the left partition)
      while (arr[leftPointer] < pivot) {
        leftPointer += 1;
			}

			// similarly, stop the right pointer as soon as we find an out of place element for the right partition
      while (arr[rightPointer] > pivot) {
        rightPointer -= 1;
      }

      // if left pointer has crossed the right pointer, break out of the main loop
      if (leftPointer >= rightPointer) {
				break;
      } else {

				// swap the values at the pointers, increment the left pointer, and continue the main loop
        [ arr[leftPointer], arr[rightPointer] ] = [arr[rightPointer], arr[leftPointer] ];
				leftPointer += 1;
			}

		}

		// once out of the main loop, swap the pivot with the current left index,
    // and return the left index, which is now the index of the pivot

    [ arr[leftPointer], arr[pivotIndex] ] = [ arr[pivotIndex], arr[leftPointer] ];

    return leftPointer;

}
