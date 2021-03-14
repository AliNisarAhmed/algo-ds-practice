def removeDups2(list):
	result = []
	for i in list:
		if i not in result:
			result.append(i)
	return result

def removeDups(arr):
	return list(set(arr))

print(removeDups2([1, 2, 3, 1, 2, 3]))