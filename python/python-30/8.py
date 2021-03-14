
def winCondition(ms1, ms2):
	(p1, m1) = ms1
	(p2, m2) = ms2
	if (m1 == "rock" and m2 == "scissors") or (m1 == "scissors" and m2 == "paper") or (m1 == "paper" and m2 == "rock"):
		 return p1
	return winCondition(ms2, ms1)

while True:
	player1 = str(input("Player 1 move: "))
	player2 = str(input("Player 2 move: "))

	winner = winCondition(("Player 1", player1), ("Player 2", player2))

	print(winner + " wins!")

	restart = str(input("New game? "))

	if (restart != "yes"):
		break



