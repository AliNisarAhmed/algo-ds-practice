number = int(input("Enter a number"))

if number % 2 == 0:
	print("The number you entered is even")
else:
	print("The number you entered is odd")

if (number % 4 == 0):
	print("The number is a multiple of 4 as well")
else:
	print("The number is not a multiple of 4")

print("Now enter two numbers: ")
num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))

if num2 % num1 == 0:
	print("num2 divides num1")
else:
	print("num2 does not divide num1")