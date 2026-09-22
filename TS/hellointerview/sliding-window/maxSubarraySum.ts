function maxSubarraySum(nums: number[], k: number): number {
  let start = 0;
  let windowSum = 0;
  let maxSum = 0;

  for (let end = 0; end < nums.length; end++) {
    windowSum += nums[end];

    if (end - start + 1 === k) {
      maxSum = Math.max(maxSum, windowSum);
      windowSum -= nums[start];
      start++;
    }
  }

  return maxSum;
}
