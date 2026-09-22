package main

import "sort"

func TriangleNumber(nums []int) int {
	sort.Ints(nums)

	count := 0
	for i := len(nums) - 1; i >= 2; i-- {
		left := 0
		right := i - 1

		for left < right {
			if nums[left]+nums[right] > nums[i] {
				count += right - left
				right--
			} else {
				left++
			}
		}
	}

	return count
}
