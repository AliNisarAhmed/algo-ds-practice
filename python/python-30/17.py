from random import randrange

def game(guess):
	userNumber = str(input())
	cows = 0
	bulls = 0
	for i in range(len(guess)):
		if guess[i] == userNumber[i]:
			cows += 1

	if cows == 4:
		print("You guesses the number!")
		return
	for i in range(len(userNumber)):
		if guess[i] != userNumber[i] and userNumber[i] in guess:
			bulls += 1
	print(f"{cows} cows, {bulls} bulls")
	game(guess)

if __name__ == "__main__":
	guess = str(randrange(1000, 9999))
	print(guess)
	print("Enter a 4-digit number")
	game(guess)

