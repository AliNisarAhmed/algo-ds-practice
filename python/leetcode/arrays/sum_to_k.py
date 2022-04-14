def sum_to_k(arr, k):
	return sum_to_k_rec(arr, k, 0, len(arr) - 1)

def sum_to_k_rec(arr, k, start, stop):
	if start >= stop:
		return False
	else:
		sum = arr[start] + arr[stop]
		if sum > k:
			return sum_to_k_rec(arr, k, start, stop - 1)
		elif sum < k:
			return sum_to_k_rec(arr, k, start + 1, stop)
		else:
			return True

print(sum_to_k([1, 2, 3, 4, 5, 6, 7, 8, 9], 100))