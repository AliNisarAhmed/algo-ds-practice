def unique(nums):
	num_set = set()
	for n in nums:
		if n in num_set:
			return False
		else:
			num_set.add(n)
	return True

def unique_rec(nums, index = 0):
	l = len(nums)

	if l == 0 or l == 1 or index == l - 1:
		return True
	rest_uniq = unique_rec(nums, index + 1)

	if not rest_uniq:
		return False

	if nums[index] in nums[index + 1:]:
		return False

	return True

