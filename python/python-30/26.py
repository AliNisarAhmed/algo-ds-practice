def checkWinner(board):
	# check rows
	for row in board:
		winner = allSame(row)
		if winner is not None:
			return winner

	# check cols

	for i in range(len(board)):
		e1 = board[0][i]
		e2 = board[1][i]
		e3 = board[2][i]
		if e1 == e2 and e2 == e3 and e3 == e1:
			return e1

	# check diagonals

	e1 = board[0][0]
	e2 = board[1][1]
	e3 = board[2][2]

	if e1 == e2 and e2 == e3 and e3 == e1:
		return e1

	e4 = board[0][2]
	e5 = board[2][0]

	if e2 == e4 and e4 == e5 and e5 == e2:
		return e2

	return 0

def allSame(arr):
	result = arr[0]
	for i in range(1, len(arr)):
		if result != arr[i]:
			return None
	return result

winner_is_2 = [[2, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	[2, 1, 0],
	[2, 1, 1]]

no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 2]]

also_no_winner = [[1, 2, 0],
	[2, 1, 0],
	[2, 1, 0]]

print(checkWinner(winner_is_1)) # 1
print(checkWinner(winner_is_2)) # 2
print(checkWinner(winner_is_also_1)) # 1
print(checkWinner(no_winner)) # 0
print(checkWinner(also_no_winner)) # 0