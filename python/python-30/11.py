def getFactors(n):
	return [k for k in range(2, (n // 2) + 1) if n % k == 0]

def isPrime(n):
	return getFactors(n) == []

print(isPrime(6))