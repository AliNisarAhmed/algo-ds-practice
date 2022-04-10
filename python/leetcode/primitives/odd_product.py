def odd_product(nums):
	for i in nums:
		if i % 2 == 1:
			for j in nums:
				if (i * j) % 2 == 1:
					return True
	return False