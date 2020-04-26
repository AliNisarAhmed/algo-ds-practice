function selectionSort(arr) {
  for (let i = 0; i < arr.length; i++) {
    let min = i;
    for (let j = i + 1; j < arr.length; j++) {
      if (arr[j] < arr[min]) {
        min = j;
      }
    }
    if (i !== min) {
      [ arr[i], arr[min] ] = [ arr[min], arr[i] ];
    }
  }
  return arr;
}

console.log(selectionSort([1, 4, 5, 6, 7, 4, 3, 2, 5, 6, 7, 8]));