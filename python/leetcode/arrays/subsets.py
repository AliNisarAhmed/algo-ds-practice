def power_set(s):
	if len(s) == 0:
		return [[]]
	first = s[0]
	rem = s[1:]
	subsets = []
	for item in power_set(rem):
		subsets.append(item)
		print(item)
		subsets.append(item[:] + [first])
		print(item[:] + [first])
	return subsets

print(power_set([1, 2, 3]))

