import { expect, test } from 'bun:test';

class Solution {
  threeSum(nums: number[]): number[][] {
    nums.sort((a, b) => a - b);
    const result: number[][] = [];

    for (let i = 0; i < nums.length - 2; i++) {
      if (i > 0 && nums[i] == nums[i - 1]) {
        continue;
      }

      let left = i + 1;
      let right = nums.length - 1;

      while (left < right) {
        const total = nums[i] + nums[left] + nums[right];

        if (total > 0) {
          right--;

        } else if (total < 0) {
          left++;
        } else {
          result.push([nums[i], nums[left], nums[right]]);
          while (left < right && nums[left] === nums[left + 1]) {
            left++;
          }
          while (left < right && nums[right] === nums[right - 1]) {
            right--;
          }
          left++;
          right--;
        }
      }
    }

    return result;
  }
}

(() => {
  const s = new Solution();
  const nums = [-1, 0, 1, 2, -1, -1];
  const result = s.threeSum(nums)
  expect(result).toEqual([[-1, -1, 2], [-1, 0, 1]])
})();
