def three_inputs():
	a = int(input("Please enter a: "))
	b = int(input("Please enter b: "))
	c = int(input("Please enter c: "))
	return (a + b == c) or (a == b - c) or (a * b == c)