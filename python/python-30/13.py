def fibonacci(n):
	a = b= 1

	if n == 0: return []
	if n == 1: return [1]

	result = [1, 1]
	while n - 2 > 0:
		result.append(a + b)
		a, b = b, a + b
		n -= 1
	return result

number = int(input("Number of fibonacci numbers? "))
print(fibonacci(number))
