# R-5.7
def find_repeating_integer(arr):
    s = sum(arr)
    print(s)
    n = len(arr)
	# from sum of first n ints = n ( n + 1) / 2
    return int(s - (n * (n - 1) / 2))


print(find_repeating_integer([1, 2, 3, 4, 5, 5, 6, 7, 8]))
