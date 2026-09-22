package main

func TwoSum(nums []int, target int) bool {
	left, right := 0, len(nums)-1

	for left < right {
		currentSum := nums[left] + nums[right]
		if currentSum == target {
			return true
		}

		if currentSum < target {
			left++
		} else {
			right--
		}
	}

	return false
}
