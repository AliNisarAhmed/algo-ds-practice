def readFile(path):
	result = []
	with open(path, 'r') as open_file:
		line = open_file.readline()
		result.append(int(line.strip('\n')))
		while line:
			line = open_file.readline()
			stripped = line.strip('\n')
			if len(stripped) > 0:
				result.append(int(stripped))

		return result

def findCommon(arr1, arr2):
	result = []
	i = 0
	j = 0
	while i < len(arr1) and j < len(arr2):
		c1 = arr1[i]
		c2 = arr2[j]
		if c1 == c2:
			result.append(c1)
			i += 1
			j += 1
		elif c1 < c2:
			i += 1
		else:
			j += 1
	return result

primes = readFile('./data/primenumbers.txt')
happies = readFile('./data/happynumbers.txt')

print(findCommon(primes, happies))

