def reverse(arr, start, stop):
	if start < stop - 1:
		arr[start], arr[stop - 1] = arr[stop - 1], arr[start]
		reverse(arr, start + 1, stop - 1)

arr = [ 1, 2, 3]
reverse(arr, 0, 3)
print(arr)