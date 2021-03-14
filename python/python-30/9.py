import random

target = random.randrange(1, 10)

while True:

	inp = input("enter a number between 1 and 9 inclusive: ")

	if input == "exit":
		break
	guess = int(inp)

	if guess < target:
		print("you guessed too low")
	elif guess > target:
		print("you guessed too high")
	else:
		print("You guessed the number!")
		print("Let's play it again")
