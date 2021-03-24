def binarySearch(arr, target):
	i = 0
	j = len(arr) - 1

	while i <= j:
		midpoint = (i + j) // 2
		current = arr[midpoint]

		if target < current:
			j = midpoint

		elif target > current:
			i = midpoint + 1

		else:
			return midpoint

	return -1

print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8], 9))