def find_repeating_integer(arr):
	s = sum(arr)
	print(s)
	n = len(arr)
	return s - (n * (n - 1) / 2)

print(find_repeating_integer([1, 2, 2, 3, 4, 5]))
