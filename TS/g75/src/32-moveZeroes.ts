function moveZeroesExtra(nums: number[]) {
  let extra = Array.from({ length: nums.length }, () => 0);

  let currPos = 0;
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      extra[currPos] = nums[i];
      currPos++;
    }
  }

  return extra;
}

function moveZeroes(nums: number[]) {
  let lastNonZeroPos = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] !== 0) {
      nums[lastNonZeroPos] = nums[i];
      lastNonZeroPos++;
    }
  }

  for (let i = lastNonZeroPos; i < nums.length; i++) {
    nums[i] = 0;
  }
}

const arr = [0, 1, 0, 3, 12];
// const arr = [1, 0];
moveZeroes(arr);
console.log(arr);
