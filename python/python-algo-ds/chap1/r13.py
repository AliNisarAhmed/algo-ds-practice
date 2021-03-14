def is_even(n):
	i = 2
	while i <= n:
		if i == n:
			return True
		i += 2
	return False
print(is_even(77))