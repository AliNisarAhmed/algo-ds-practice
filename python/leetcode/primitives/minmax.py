def minmax(nums):
	min = max = nums[0]
	for n in nums:
		if n < min:
			min = n
		elif n > max:
			max = n
	return (min, max)