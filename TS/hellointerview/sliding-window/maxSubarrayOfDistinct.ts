class Solution {
  maxSum(nums: number[], k: number): number {

    let maxSum = 0;
    let seen = new Set();
    let currentSum = 0;

    let start = 0;

    for (let end = 0; end < nums.length; end++) {
      while (seen.has(nums[end])) {
        currentSum -= nums[start];
        seen.delete(nums[start]);
        start++;
      }

      currentSum += nums[end];
      seen.add(nums[end]);

      if (end - start + 1 === k) {
        maxSum = Math.max(maxSum, currentSum);
        currentSum -= nums[start];
        seen.delete(nums[start]);
        start++;
      }
    }

    return maxSum;
  }
}
