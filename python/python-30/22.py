def readFile(path):
	result = []
	with open(path, 'r') as open_file:
		line = open_file.readline()
		result.append(line.strip('\n'))
		while line:
			line = open_file.readline()
			result.append(line.strip('\n'))
		return result

print(readFile('./data/nameslist.txt'))

def countNames(arr):
	result = {}
	for name in arr:
		if name in result:
			result[name] += 1
		else:
			result[name] = 1
	return result

print(countNames(readFile('./data/nameslist.txt')))