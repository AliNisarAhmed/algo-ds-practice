from random import randint

def shuffle(data):
	length = len(data)
	res = [None] * length
	used_indices = set()
	for i in range(length):
		added = False
		while added == False:
			choice = randint(0, length - 1)
			if choice not in used_indices:
				res[choice] = data[i]
				used_indices.add(choice)
				added = True
	return res

def shuffle(data):
	# use fisher-yates algo
	length = len(data)
	for i in range(length - 1, 0, -1):
		j = randint(0, i)
		data[i], data[j] = data[j], data[i]
