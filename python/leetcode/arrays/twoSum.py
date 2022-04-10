class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		if len(nums) < 2:
			return []
		vals = {}
		for i in range(len(nums)):
			current = nums[i]
			complement = target - current
			if current not in vals:
				vals[current] = i
			if complement in vals and vals[complement] != i:
				return [i, vals[complement]]
