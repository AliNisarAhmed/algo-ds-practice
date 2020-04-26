
function bubbleSort(arr) {
  for (let i = arr.length - 1; i >= 0; i--) {
    let swaps = false;
    for (let j = 0; j < i; j++) {
      if (arr[j] > arr[j + 1]) {
        [ arr[j], arr[j + 1] ] = [ arr[j + 1], arr[j] ];
        swaps = true;
      }
      console.log('Inside iteration: ', j)
    }
    console.log('outside iteration: ', i)
    if (!swaps) break;
  }

  return arr;
}

console.log(bubbleSort([1, 2, 3, 4, 7, 8, 6, 9, 10]))