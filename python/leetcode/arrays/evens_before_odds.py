def evens_before_odds(nums, index = 0):
	if index >= len(nums):
		return []
	else:
		if nums[index] % 2 == 0:
			# even
			return [nums[index]] + evens_before_odds(nums, index + 1)
		else:
			return evens_before_odds(nums, index + 1) + [nums[index]]

print(evens_before_odds([1, 2, 3, 4, 5]))