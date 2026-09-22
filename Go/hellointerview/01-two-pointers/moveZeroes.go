package main

func MoveZeroes(nums []int) {
	nextNonZeroSpot := 0

	for i, n := range nums {
		if n != 0 {
			nums[nextNonZeroSpot], nums[i] = nums[i], nums[nextNonZeroSpot]
			nextNonZeroSpot++
		}
	}
}
