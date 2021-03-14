def common(arr1, arr2):
	result = []
	for elem in arr1:
		if elem in arr2:
			result.append(elem)
	return result

print(common([1, 2, 3], [2, 3, 4]))