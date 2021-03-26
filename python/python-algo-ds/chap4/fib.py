def bad_fib(n):
	if n <= 1: return 1
	return bad_fib(n - 1) + bad_fib(n - 2)

def good_fib(n):
	if n <= 1: return (n, 0)
	else:
		(a, b) = good_fib(n - 1)
		return (a + b, a)