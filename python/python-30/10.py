def common(arr1, arr2):
	return [k for k in set(arr1) if k in arr2]

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(common(a, b))