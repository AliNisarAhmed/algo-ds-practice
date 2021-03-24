def guessNumber():
	turns = 0
	i = 0
	j = 100
	guess = 50
	yes_responses = ["y", "yes", "ok", "done"]
	response = None
	while i <= j:
		turns += 1
		print(f"my guess is {guess}")
		r = input("is this your number? (y)es/(n)o ")
		if r in yes_responses:
			print(f"I guessed your number in {turns} turns.")
			return
		r = input("is the number higher? (y)es/(n)o ")
		if r in yes_responses:
			i = guess
		else:
			j = guess
		guess = (i + j) // 2
	print("Your number is not between 0 and 100 for sure.")

guessNumber()