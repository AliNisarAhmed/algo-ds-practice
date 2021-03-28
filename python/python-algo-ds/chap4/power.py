def power2(x, n):
	if n == 0:
		return 1
	return x * power2(x, n - 1)


# uses 2^13 = 2 . 2^6 . 2^6
def power(x, n):
	if n == 0:
		return 1

	else:
		partial = power(x, n // 2)
		result = partial * partial
		if n % 2 == 1:  # if n is odd, multiply by x once more
			result *= x
		return result
