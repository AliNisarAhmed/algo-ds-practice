function maxArea(arr) {
  let left = 0;
  let right = arr.length - 1;

  let maxArea = 0;
  while (left < right) {
    currentArea = calcArea(left, arr[left], right, arr[right]);
    maxArea = Math.max(maxArea, currentArea);

    if (arr[left] < arr[right]) {
      left++;
    } else {
      right--;
    }
  }

  return maxArea;
}

function calcArea(i, ai, j, aj) {
  return (j - i) * Math.min(ai, aj);
}
