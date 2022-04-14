def tower_of_hanoi(n, origin, destination, buffer):
	if n > 0:
		tower_of_hanoi(n - 1, origin, buffer, destination)
		move_top(origin, destination)
		tower_of_hanoi(n - 1, origin, destination, buffer)

def move_top(origin, destination):
	destination.append(origin.pop)