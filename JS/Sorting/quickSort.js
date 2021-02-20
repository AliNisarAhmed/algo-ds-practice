function quickSort(arr, left = 0, right = arr.length - 1) {
	if (left < right) {
		const pivotIndex = helper(arr, left, right);
		// left side
		quickSort(arr, left, pivotIndex - 1);
		// right side
		quickSort(arr, pivotIndex + 1, right);
	}
	return arr;
}

function helper(arr, start = 0, end = arr.length - 1) {
	let pivot = arr[start];
	let pivotIndex = start;
	for (let i = start + 1; i <= end; i++) {
		if (pivot > arr[i]) {
			pivotIndex++;
			[ arr[i], arr[pivotIndex] ] = [ arr[pivotIndex], arr[i] ];
		}
	}

	[ arr[start], arr[pivotIndex] ] = [ arr[pivotIndex], arr[start] ];
	return pivotIndex;
}

// console.log(quickSort([1, 8, 3, 2, 9, 7, 6, 5, 4]));
console.log(quickSort([8, 2, 5, 3]));


// --------------   Method 2 -------------------

// here, we choose the last element as the pivot

function quickSort2(arr, left = 0, right = arr.length - 1) {
	if (left < right) {
		const pivotIndex = partition(arr, left, right);
		quickSort2(arr, left, pivotIndex - 1);
		quickSort2(arr, pivotIndex + 1, right);
	}

	return arr;
}

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


