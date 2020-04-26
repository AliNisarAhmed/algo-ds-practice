function insertionSort(arr) {

  for (let i = 0; i < arr.length; i++) {
    let j = i + 1;

    while(arr[j] < arr[j - 1] && j > 0) {
      [ arr[j], arr[j - 1] ] = [ arr[j - 1], arr[j] ];
      j--;
    }
  }

  return arr;
}

console.log(insertionSort([2, 1, 9 , 76, 4]))