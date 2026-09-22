package main

func MaxArea(heights []int) int {
	left, right := 0, len(heights)-1

	result := 0

	for left < right {
		currentArea := (left - right) * min(heights[left], heights[right])

		if currentArea > result {
			result = currentArea
		}

		if heights[left] < heights[right] {
			left++
		} else {
			right--
		}
	}

	return result
}
