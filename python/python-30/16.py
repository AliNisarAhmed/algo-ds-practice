from random import choice, shuffle

def genSmallCase():
	return choice("abcdefghijklmnopqrstuvwxyz")

def genUpperCase():
	return choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def genNumber():
	return choice("1234567890")

def genSpecial():
	return choice("!@#$%^&*()")

def genPassword(n):
	if (n < 5): raise ValueError("Minimum password length is 5")
	result = ''
	for i in range(n - 3):
		result += genSmallCase()
	result += genUpperCase()
	result += genNumber()
	result += genSpecial()
	shuffle(list(result))
	print(result)
	return ''.join(result)

n = int(input("password length: "))
print(genPassword(n))