def power(x, n):
	if n == 0:
		return 1
	else:
		partial = power(x, n // 2)
		result = partial * partial
		if n % 2 == 1:
			result *= x
		return result

# iterative

def power_iter(x, n):
	result = 1
	for i in range(n // 2):
		result *= x * x
	if n % 2 == 1:
		result *= x
	return result

print(power_iter(2, 6))