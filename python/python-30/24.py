def printDashes(n = 1):
	print(' ', end="")
	for i in range(n):
		for j in range(n):
			print('-', end="")
		print(' ', end="")
	print('')

def printBars(n = 1):
	print('|', end="")
	for i in range(n):
		for j in range(n):
			print(' ', end="")
		print('|', end="")
	print('')

def printBoard(n = 3):
	for i in range(2 * n + 1):
		if i % 2 == 0:
			printDashes(n)
		else:
			printBars(n)

printBoard(8)