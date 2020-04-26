function merge(arr1, arr2) {
  let i = 0;
  let j = 0;
  const result = [];

  while (true) {
    if (i === arr1.length) {
      result.push(...arr2.slice(j));
      break;
    }  else if (j === arr2.length) {
      result.push(...arr1.slice(i));
      break;
    } else if (arr1[i] < arr2[j]) {
      result.push(arr1[i]);
      i++;
    } else if (arr1[i] > arr2[j]) {
      result.push(arr2[j]);
      j++;
    } else {
      result.push(arr1[i], arr2[j]);
      i++;
      j++;
    }
  }
  return result;
}

function mergeSort(arr) {
  if (arr.length === 1) return arr;

  const midpoint = Math.floor(arr.length / 2);
  return merge(mergeSort(arr.slice(0, midpoint)), mergeSort(arr.slice(midpoint)));
}

console.log(mergeSort([3, 4, 2, 1]));