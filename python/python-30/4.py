def getFactors(n):
	return [k for k in range(2, (n // 2) + 1) if n % k == 0]

number = int(input("Give me an integer: "))

factors = getFactors(number)

for f in factors:
	print(f)