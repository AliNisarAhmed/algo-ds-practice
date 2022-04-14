def product(m, n = 1):
	if m == 0 or n == 0:
		return 0
	if n == 1:
		return m
	return m + product(m, n - 1)