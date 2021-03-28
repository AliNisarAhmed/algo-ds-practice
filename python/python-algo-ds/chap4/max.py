def myMax(arr):
	if len(arr) == 1:
		return arr[0]
	return max(arr[0], myMax(arr[1:]))

print(myMax([1, 2, 3, 4]))