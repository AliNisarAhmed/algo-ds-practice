def minmax(nums):
	min = max = nums[0]
	for n in nums:
		if n < min:
			min = n
		elif n > max:
			max = n
	return (min, max)

# Recursive

def minmax_rec(nums = [], index = 0, minimum = nums[0], maximum = nums[0]):
	l = len(nums)
	if l == 0 or index == l - 1:
		return (minimum, maximum)
	else:
		minmax(nums, index + 1, min(nums[index], min), max(maximum, nums[index]))


def minmax_rec(nums, index = 0):
	l = len(nums)
	if l == 0 or index == l - 1:
		return (nums[index], nums[index])
	else:
    min_r, max_r = minmax_rec(nums, index + 1)
    return (min(nums[index], min_r), max(nums[index], max_r))