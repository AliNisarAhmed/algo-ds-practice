function search(nums, target) {

  let start = 0;
  let end = nums.length - 1;

  while (start < end) {
    let mid = Math.floor(start + (end - start) / 2);

    let current = nums[mid];

    if (target < current) {
      end = mid - 1;
    } else if (target > current) {
      start = mid + 1;
    } else {
      return mid;
    }
  }

  return -1;
}

console.log(search([-1, 0, 3, 5, 9, 12], 9));
