from typing import List

class Solution:
	def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
		maxSoFar = 0
		count = 0
		for i in range(len(nums)):
			if nums[i] == 1:
				count += 1
			else:
				maxSoFar = max(maxSoFar, count)
				count = 0
		return max(maxSoFar, count)

s = Solution()
print(s.findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))