def sum_of_squares(n):
	sum = 0
	for i in range(1, n):
		sum += i * i
	return sum

def sum_of_squares_2(n):
	return sum(x * x for x in range(1, n))

def sum_of_squares_odd(n):
	return sum(x * x for x in range(1, n) if x % 2 == 1)