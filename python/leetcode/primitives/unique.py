def unique(nums):
	num_set = set()
	for n in nums:
		if n in num_set:
			return False
		else:
			num_set.add(n)
	return True